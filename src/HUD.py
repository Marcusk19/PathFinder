#!/usr/bin/env python3
# Main code for HUD Display
# Marcus Kok 1/16/22
# [TODO] setup communication between app and phone

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
    print("Connected with result: " + str(rc))
    client.subscribe([("source", 0), ("destination", 0)])
    client.message_callback_add("source", on_source)
    client.message_callback_add("destination", on_dest)


def on_message(client, userdata, msg):
    print("msg topic: " + str(msg.payload))

# mqtt msg.payload comes in as b'message'
def on_source(client, userdata, msg):
    global inputA, inputB
    inputA = str(msg.payload)
    inputA = inputA[2 : len(inputA)-1] # get rid of mqtt formatting
    print("inputA = " + inputA)

def on_dest(client, userdata, msg):
    global inputB, inputA
    inputB = str(msg.payload)
    inputB = inputB[2 : len(inputB)-1] # get rid of mqtt formatting
    print("inputB = " + inputB)


def pull_directions():
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

    screen.show_direction(instructions[0])
    

main()



