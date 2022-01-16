# Main code for HUD Display
# Marcus Kok 1/16/22

import os
from tkinter import *
from tkinter import ttk 

print('Hello World');

master = Tk()

Label(master, text='Enter your name').grid(row=0)
Label(master, text='Enter your email').grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop()



