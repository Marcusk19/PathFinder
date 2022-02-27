#rough code for ODB setup
#Jackson + Marcus
#2/27/22

import obd
from obd import OBDStatus as status
import time

#Attempt to establish a connection and initialize a timer to keep track of wait cycles.
class Obd:
    def __init__(self):
        """ Constructor for class. Attempts to form a connection. It has to loop multiple times to pull all instructions, which is what the while Loop does."""
        obd.logger.setLevel(obd.logging.DEBUG)
        print("Attempting to establish connection")

        self.connection = obd.OBD(portstr="/dev/rfcomm0", protocol='6', fast=False)
        while (len(self.connection.supported_commands) < 100):
	        self.connection = obd.OBD(portstr="/dev/rfcomm0", protocol='6', fast=False)
        
        checkpoint = self.connection.status()
        
        print("Connection formed.")
        print("Connection status is: ", checkpoint)

        self.speedInKilo = 0;

    def get_speed(self):
        """ Queries speed of car is connected """
        if self.connection.status() == status.CAR_CONNECTED: #If the car is connected and turned on
            speed = self.connection.query(obd.commands.SPEED) #Queries the speed, object with a value in kilometers per hour.

            if speed is None:
                return "Could not obtain speed"
            else:
                self.speedInKilo = speed  # converts speed from kilo to miles
                # in the meantime, print results for debugging purposes
                return self.speedInKilo

    def get_fuel_percentage(self):
        """ Queries fuel % of car is connected """
            self.fuelPercentage = self.connection.query(obd.commands.FUEL_LEVEL).value #Returns a % of fuel
            if self.fuelPercentage is None:
                return "Could not pull fuel percentage"
            else:
                return self.fuelPercentage

reciever = Obd()
""" While loop that relies on previous functions to show the user what is occuring. """
while True:
  fuel = str(reciever.get_fuel_percentage())
  speed = str(reciever.get_speed())
  speedstring = "Speed is:" + speed
  fuelstring = "Fuel percentage is: " + fuel
  print(speedstring)
  print(fuelstring)
  print("Updating...")
  time.sleep(1)  
