#!/usr/bin/env python
import math
import time
import subprocess
from PIL import Image, ImageDraw, ImageFont
from board import SCL, SDA
import busio
import adafruit_ssd1306

class Display():
        def __init__(self):
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
                # Draw a black filled box to clear the image.
                self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
                self.refresh()
        
        def refresh(self):
                self.disp.image(self.image)
                self.disp.show() 


        def show_text(self, text="not available"):
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
                testfont = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefont/Georgia.ttf", 8)
                self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
                self.draw.text((0, top), "Turn left on", font=testfont, fill=255)
                self.draw.text((0, top+8), "Entrepreneur Drive", font=testfont, fill=255)
                self.draw.text((0, top+16), "in 1 mile", font=testfont, fill=255)
                self.refresh()
        
        def show_direction(self, text):
                words = text.split()
                lines = []
                wpl = len(words) / 4
                prev = 0 # save prev index for iteration
                if(len(words) % 4 == 0):
                        for i in range (0, 4):
                                lines.append(words[int(prev):int(prev+wpl)])
                                prev = i+wpl # increment prev
                else:
                        for i in range (0,3):
                                lines.append(words[int(prev):int(prev+wpl)])
                                prev = i+wpl # increment prev
                        lines.append(words[int(prev):int(prev+wpl + (len(words)%4))])

                self.clear_disp() # clear display for words
                testfont = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefont/Georgia.ttf", 8)
                top = -2
                for i in range (0, 4):
                        self.draw.text((0, (top + i*8)), lines[i].join(" "), font=testfont, fill=255)
                
                self.refresh()
  

                
                


