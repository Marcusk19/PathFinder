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

    controller = DirectionController(locA, locB)
    controller.getDirections()

    instructions = controller.getInstructions()
    
    if len(instructions) == 0:
        print("Directions could not be found")

    for instruction in instructions:
        print(instruction)

main()



