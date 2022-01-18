#!/usr/bin/env python3
# Main code for HUD Display
# Marcus Kok 1/16/22


import os, sys, getopt
import tkinter as tk
from tkinter import BOTH, Canvas, W
import directions

def main():
    # instance of directionController
    input_A = sys.argv[1]
    input_B = sys.argv[2]

    dirC = directions.directionController

    locA = str(input_A).replace(' ', '&')
    locB = str(input_B).replace(' ', '&')

    dirMessage = dirC.sayHello()
    print("Directions from " + str(input_A) + " to " + str(input_B))
    dirC.getDirections(locA, locB)

    instructions = dirC.getInstructions()
    for instruction in instructions:
        print(instruction)

main()



