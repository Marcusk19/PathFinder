#!/usr/bin/env python3
# Main code for HUD Display
# Marcus Kok 1/16/22
""" 
HUD Module
----------

Main module for running PathFinder software.

This module calls from display, directions, and OBD to 
put together fucntionality for the PathFinder project.
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
from ast import While
import os, sys, getopt
from directions import DirectionController
import paho.mqtt.client as mqtt
import display

inputA = ""
inputB = ""
client = mqtt.Client() # instance of Client object

def main():
    """ Main function of PathFinder project. Sets up connection to 
    MQTT broker and calls functions defined below.
    """
    MQTT_SERVER = "45.56.117.102" # ip address of linode instance
    
    client.on_connect = on_connect # override methods
    client.on_message = on_message

    client.connect(MQTT_SERVER) # connect to broker
    client.loop_start() # start new thread loop to handle network
    print("Waiting on user input...")

    while True:
        if inputA != "" and inputB != "":
            break;

    pull_directions()
    client.loop_stop()


def on_connect(client, userdata, flags, rc):
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
    client.message_callback_add("source", on_source) 
    client.message_callback_add("destination", on_dest)


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
def on_source(client, userdata, msg):
    """ Defines what should happen upon receiving a message published
    on the 'source' channel.
    Formats message payload and saves to local variable inputA.

    Args:
        client (client): MQTT client class instance.
        userdata (userdata): A user provided object passed to the on_message callback.
        msg (msg): Message class from the broker.
    """
    global inputA, inputB
    inputA = str(msg.payload)
    inputA = inputA[2 : len(inputA)-1] # get rid of mqtt formatting
    print("inputA = " + inputA)

def on_dest(client, userdata, msg):
    """ Defines what should happen upon receiving a message published
    on the 'destination' channel.
    Formats message payload anad saves to local variable inputB.

    Args:
        client (client): MQTT client class instance.
        userdata (userdata): A user provided object passed to the on_message callback when a message is received.
        msg (msg): Message class from the broker.
    """
    global inputB, inputA
    inputB = str(msg.payload)
    inputB = inputB[2 : len(inputB)-1] # get rid of mqtt formatting
    print("inputB = " + inputB)


def pull_directions():
    """ Method instantiates a DirectionController and Display instance.
    Calls getDirections() and getInstructions from DirectionController then 
    formats them for Display.
    """
    # massage inputs (spaces replaced with &)
    locA = str(inputA).replace(' ', '&')
    locB = str(inputB).replace(' ', '&')

    print("Directions from " + str(inputA) + " to " + str(inputB))

    # initialize instance of DirectionController from directions.py
    controller = DirectionController(locA, locB)
    controller.getDirections()

    screen = display.Display(); # instance of display

    # Call handler function to get instructions
    instructions = controller.getInstructions()
    
    # empty list means directions were unable to be found
    if len(instructions) == 0:
        print("Directions could not be found")

    # print out instruction by instruction
    for instruction in instructions:
        print(instruction)
    # call display to show the directions
    screen.show_direction(instructions[0])
    
# call main function
if __name__ == '__main__':
    main()



