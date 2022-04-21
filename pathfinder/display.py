#!/usr/bin/env python
"""
Display Module
------------------
This is a module to control the OLED display for the PathFinder via I2C protocol.

Typical usage example:
        screen = display.Display()
"""
import math
import time
import subprocess
from PIL import Image, ImageDraw, ImageFont
from board import SCL, SDA
import busio
import adafruit_ssd1306

class Display():
        """ Base class for display.
        Defines the basic properties of the display plus methods used
        to update an OLED display using I2C interface with text output. 

        Attributes
        ----------
        i2c:
                Defines bus supported I2C protocol.
        disp:
                Object represented from adafruit OLED display drivers
        """
        def __init__(self):
                """ initializes i2c interface, display, and window """
                i2c = busio.I2C(SCL, SDA)
                self.disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
                self.disp.fill(0)
                self.disp.show()
                i2c = busio.I2C(SCL, SDA)
                self.width = self.disp.width
                self.height = self.disp.height
                self.image = Image.new("1", (self.width, self.height))
                self.draw = ImageDraw.Draw(self.image)
                self.font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefont/Georgia.ttf", 20)
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.

        
        def clear_disp(self):
                """ Clears the display image
                """
                # Draw a black filled box to clear the image.
                self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
                self.refresh()

        def clear_bot(self):
                self.draw.rectangle((0, 24, self.width, 32), outline=0, fill=0)
                self.refresh()
        
        def clear_mid(self):
                self.draw.rectangle((0, 16, self.width, 24), outline=0, fill=0)
                self.refresh()
        
        def refresh(self):
                """ Refreshes the display to show a new image. 
                Specifically places image in display and calls
                disp.show() to present the image.
                """
                self.disp.image(self.image)
                self.disp.show() 

        # Note: this function was only used in testing and should not be used for anything else
        def show_text(self, text="not available"):
                """ 
                Shows line of text

                Args:
                        text (string): text to put on display, defaults to 'not available'
                """
                self.clear_disp()
                # Load default font.
                
                # Draw text.
                self.draw.text((0, 5), "PATHFINDER", font=self.font, fill=255)
                # Display image.
                self.disp.image(self.image)
                self.disp.show()
                # Pause briefly before drawing next frame.
                time.sleep(3)
                font = ImageFont.load_default()

                padding = -2
                top = padding
                bottom = self.height - padding
                x = 0
                testfont = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefont/Georgia.ttf", 10)
                self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
                self.draw.text((0, top), "Turn left on", font=testfont, fill=255)
                self.draw.text((0, top+8), "Entrepreneur Drive", font=testfont, fill=255)
                self.draw.text((0, top+16), "in 1 mile", font=testfont, fill=255)
                self.refresh()
        
        def show_direction(self, text):
                """ 
                Takes instruction input and splits into 3 lines for display
                
                Args:
                        text (string): String containing instruction.
                """
                words = text.split()
                lines = []
                wpl = len(words) / 2
                prev = 0 # save prev index for iteration
                # We want to split the amount of words evenly across the display
                # There are two cases: 1 - number of words is divisible by 2
                #                      2 - number of words is NOT divisible by 2
                # In the case of the latter, we simply append the remainder(%) of 
                # words onto the last line
                if(len(words) % 2 == 0):
                        for i in range (0, 2):
                                lines.append(words[int(prev):int(prev+wpl)])
                                prev = prev+wpl # increment prev
                else:
                        for i in range (0,1):
                                lines.append(words[int(prev):int(prev+wpl)])
                                prev = prev+wpl # increment prev
                        lines.append(words[int(prev):int(prev+wpl + (len(words)%2))])

                self.clear_disp() # clear display for words
                testfont = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefont/Georgia.ttf", 8) # choosing font size
                top = 0 # buffer between lines
                for i in range (0, 2):
                        self.draw.text((0, (top + i*8)), ' '.join(lines[i]), font=testfont, fill=255) # loop for four times, place text on each line
                # refresh the display for actual output
                self.refresh()

        def show_obd(self, speed, fuel, health):
                self.clear_bot()
                # Load default font.
                
                font = ImageFont.load_default()

                padding = -2
                top = padding
                bottom = self.height - padding
                x = 0
                testfont = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefont/Georgia.ttf", 9)
                # fuel = "{:0f}".format(fuel)
                OBD_response = "F: " + str(fuel) + "% " + "    S: " + str(speed) + "    H: " + health
                self.draw.text((0, top+24), OBD_response, font=testfont, fill=255)
                self.refresh()

        def show_arrow(self, current_inst, distance):
                self.clear_mid()
                font = ImageFont.load_default()

                padding = -2
                top = padding
                bottom = self.height - padding
                x = 0
                testfont = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefont/Georgia.ttf", 9)

                arrow = ""
                if current_inst.__contains__("right"):
                        arrow = "->"
                elif current_inst.__contains__("left"):
                        arrow = "<-"
                else:
                        arrow = "^"
                
                arrow_response = arrow + " in " + str(distance) + " miles"
                self.draw.text((0, top+16), arrow_response, font=testfont, fill=255)
                self.refresh()
                

                

