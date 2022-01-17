#!/usr/bin/env python3
# Main code for HUD Display
# Marcus Kok 1/16/22


import os
import tkinter as tk
from tkinter import BOTH, Canvas, W
import directions


dirC = directions.directionController

dirMessage = dirC.sayHello()
# print(dirMessage);
dirC.getDirections("Disneyland", "Hollywood")

instructions = dirC.getInstructions()
for instruction in instructions:
    print(instruction)

# class Display(tk.Frame):
#     def __init__(self):
#         super().__init__()

#         self.initUI()
    
#     def initUI(self):
#         self.master.title("Lines")
#         self.pack(fill=BOTH, expand=1)

#         canvas = Canvas(self)
#         canvas.create_text(100, 125, anchor=W, font="Purisa",
#                             text=dirMessage)

#         canvas.pack(fill=BOTH, expand = 1)


# def main():

#     root = tk.Tk()
#     disp = Display()
#     root.geometry("400x250+300+300")
#     root.mainloop()

# if __name__ == '__main__':
#     main()


