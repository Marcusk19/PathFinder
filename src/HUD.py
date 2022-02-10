#!/usr/bin/env python3
# Main code for HUD Display
# Marcus Kok 1/16/22
# [TODO] setup communication between app and phone

import os, sys, getopt
from directions import DirectionController

def main():
    # instance of directionController
    input_A = sys.argv[1]
    input_B = sys.argv[2]

    locA = str(input_A).replace(' ', '&')
    locB = str(input_B).replace(' ', '&')

    print("Directions from " + str(input_A) + " to " + str(input_B))

    # initialize instance of DirectionController from directions.py
    controller = DirectionController(locA, locB)
    controller.getDirections()

    # Call handler function to get instructions
    instructions = controller.getInstructions()
    
    # empty list means directions were unable to be found
    if len(instructions) == 0:
        print("Directions could not be found")

    # print out instruction by instruction
    for instruction in instructions:
        print(instruction)

main()



