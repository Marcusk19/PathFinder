#!/usr/bin/env python3
# Main code for HUD Display
# Marcus Kok 1/16/22
""" 
HUD Module
----------

Main module for running PathFinder software.

This module calls from display, directions, and OBD to 
put together functionality for the PathFinder project.
Furthermore, it acts as a MQTT client subscribed to the
broker listening to channels 'source' and 'destination'

inputA:
    String representation of source point for PathFinder.
inputB:
    String representation of destination point for PathFinder.
client:
    Instance of mqtt.Client() object for subscribing to the MQTT broker.

Typical usage example:
    
    python3 pathfinder/HUD.py
"""
# imports
from directions import DirectionController
import paho.mqtt.client as mqtt
import threading
import GPS
import time
class Hud(threading.Thread):
    def __init__(self, display):
        threading.Thread.__init__(self)
        self.inputA = ""
        self.inputB = ""
        self.client = mqtt.Client() # instance of Client object
        self.instructions = []
        self.coordinates = []
        self.gps = GPS.GPS_controller()
        self.screen = display

    def run(self):
        """ Main function of PathFinder project. Sets up connection to 
        MQTT broker and calls functions defined below.
        """

        MQTT_SERVER = "45.56.117.102" # ip address of linode instance (aka MQTT broker)
        
        self.client.on_connect = self.on_connect # override methods
        self.client.on_message = self.on_message

        self.client.connect(MQTT_SERVER) # connect to broker
        self.client.loop_start() # start new thread loop to handle messaging
        print("Waiting on user input...")


        # loop here until we receive input
        while True:
            if self.inputA != "" and self.inputB != "":
                break;

        self.pull_directions()

        step = 0

        while True:
            # self.gps.gpsd.next()
            current_location = self.gps.get_coordinates()

            next_lat = float(self.coordinates[step]['lat'])
            next_lng = float(self.coordinates[step]['lng'])
            next_location = (next_lat, next_lng)
            print("Current location: " + str(current_location) + "\t Next location: " + str(next_location))
            if current_location[0] == "nan":
                distance_to_point = 10000000
            else: 
                distance_to_point = self.gps.calculate_distance(current_location, next_location)
            self.screen.show_arrow(self.instructions[step], distance_to_point)
            if distance_to_point < 0.1:
                step = step + 1
                if step > len(self.coordinates):
                    break
                self.screen.show_direction(self.instructions[step]) 

            print(distance_to_point)
            time.sleep(0.5)

        self.client.loop_stop()


    def on_connect(self, client, userdata, flags, rc):
        """ The callback for when the client recieves a CONNACK response from the server.

        Args:
            client (client): The client instance for this callback.
            userdata (userdata): The private user data set in Client() or user_data_set().
            flags (flags): Response flags sent by the broker.
            rc (rc): The connection result.
        """
        print("Connected with result: " + str(rc)) # print the result for visibility
        client.subscribe([("source", 0), ("destination", 0)]) # subscribe to channels for source and destination
        # define what happens when you get messages from channels source and destination
        client.message_callback_add("source", self.on_source) 
        client.message_callback_add("destination", self.on_dest)


    def on_message(client, userdata, msg):
        """ Callback function that happens when subscriber client receives message
        from broker.

        Args:
            client (client): Instance of client class.
            userdata (userdata): User provided object passed onto on_message callback when a message is received.
            msg (msg): Message class from the broker.
        """
        print("msg topic: " + str(msg.payload))

    # mqtt msg.payload comes in as b'message'
    def on_source(self, client, userdata, msg):
        """ Defines what should happen upon receiving a message published
        on the 'source' channel.
        Formats message payload and saves to local variable inputA.

        Args:
            client (client): MQTT client class instance.
            userdata (userdata): A user provided object passed to the on_message callback.
            msg (msg): Message class from the broker.
        """
        self.inputA = str(msg.payload)
        self.inputA = self.inputA[2 : len(self.inputA)-1] # get rid of mqtt formatting
        print("inputA = " + self.inputA)

    def on_dest(self, client, userdata, msg):
        """ Defines what should happen upon receiving a message published
        on the 'destination' channel.
        Formats message payload anad saves to local variable inputB.

        Args:
            client (client): MQTT client class instance.
            userdata (userdata): A user provided object passed to the on_message callback when a message is received.
            msg (msg): Message class from the broker.
        """
        self.inputB = str(msg.payload)
        self.inputB = self.inputB[2 : len(self.inputB)-1] # get rid of mqtt formatting
        print("inputB = " + self.inputB)


    def pull_directions(self):
        """ Method instantiates a DirectionController and Display instance.
        Calls getDirections() and getInstructions from DirectionController then 
        formats them for Display.
        """
        # massage inputs (spaces replaced with &)
        locA = str(self.inputA).replace(' ', '&')
        locB = str(self.inputB).replace(' ', '&')

        print("Directions from " + str(self.inputA) + " to " + str(self.inputB))

        # initialize instance of DirectionController from directions.py
        controller = DirectionController(locA, locB)
        controller.getDirections()

        # Call handler function to get instructions
        self.instructions = controller.getInstructions()
        self.coordinates = controller.getCoordinates()
        
        # empty list means directions were unable to be found
        if len(self.instructions) == 0:
            print("Directions could not be found")

        # print out instruction by instruction
        for instruction in self.instructions:
            print(instruction)
        for coordinate in self.coordinates:
            print(coordinate)
        # call display to show the directions
        self.screen.show_direction(self.instructions[0]) 
        
