#rough code for ODB setup
#Jackson
#1/30/2022
"""
Main module for OBD metric ingestion.

Module creates connection to bluetooth OBDII transmitter
and returns measurement values from it. 

Notes
-----
Work in progress

"""
import obd
from obd import OBDStatus as status

#Attempt to establish a connection and initialize a timer to keep track of wait cycles.
class Obd:
    def __init__(self):
        """ Calls connect() to connect to OBDII bluetooth transmitter upon instantiation.
        """
        print("Attempting to establish connection")
        obd.logger.setLevel(obd.logging.DEBUG)

        self.connection = obd.OBD(portstr="/dev/tty.OBDII", fast=False, timeout=40)
        checkpoint = self.connection.status()
        print("Connection status is: ", checkpoint)

        self.loopTimer = 0

        self.speedInMiles = 0;

    def connect():
        """ Method to initialize a connection to OBDII transmitter.
        """
        print("Attempting to establish connection")
        connection = obd.OBD(portstr="/dev/tty.OBDII", fast=False, timeout=40)
        checkpoint = connection.status()
        print("Connection status is: ", checkpoint)

    def get_speed(self):
        """ Method to return the speed in miles per hour detected from the OBDII transmitter.

        Returns:
            var: Speed in miles per hour.
        """
        if self.connection.status() == status.CAR_CONNECTED: #If the car is connected and turned on
            speedInKilo = self.connection.query(obd.commands.SPEED) #Queries the speed, object with a value in kilometers per hour.
            fuelPercentage = self.connection.query(obd.commands.FUEL_LEVEL).value #Returns a % of fuel

            if speedInKilo is None:
                return "Could not obtain speed"
            else:
                self.speedInMiles = 0.621371 * speedInKilo.value  # converts speed from kilo to miles
                # in the meantime, print results for debugging purposes
                return self.speedInMiles

    def get_fuel_percentage(self):
        """ Method to return the fuel percentage detected from OBDII transmitter.

        Returns:
            var: Fuel percentage.
        """
        self.fuelPercentage = self.connection.query(obd.commands.FUEL_LEVEL).value #Returns a % of fuel
        if self.fuelPercentage is None:
            return "Could not pull fuel percentage"
        else:
            return self.fuelPercentage

# while True:
#     if connection.status() == status.CAR_CONNECTED: #If the car is connected and turned on
#         speedInKilo = connection.query(obd.commands.SPEED) #Queries the speed, object with a value in kilometers per hour.
#         fuelPercentage = connection.query(obd.commands.FUEL_LEVEL).value #Returns a % of fuel

#         if speedInKilo is None:
#             print("Could not pull speed")
#         else:
#             speedInMiles = 0.621371 * speedInKilo.value  # converts speed from kilo to miles
#             # in the meantime, print results for debugging purposes
#             print("Speed:", speedInMiles)

#         if fuelPercentage is None:
#             print("Could not pull fuel percentage")
#         else:
#             # in the meantime, print results for debugging purposes
#             print("Fuel Percentage:", fuelPercentage)

#         if loopTimer % 600 == 0 or loopTimer == 0: #this loop will run on the very first loop, and then will run every 10 minutes after
#             errorCodes = connection.query(obd.commands.GET_DTC) #query all dtc error codes, returns a list of tuples
#             if errorCodes is None:
#                 print("No DTC Codes")
#             else:
#                 for index, tuple in enumerate(errorCodes.value): #iterates through tuple list and prints the error code (0) and the error description (1)
#                     print(tuple[0], tuple[1])

#         loopTimer += 0.5 #increases timer here to keep track of wait time

#     else:
#         print("Attempting to establish connection again.")
#         connection = obd.OBD() #attempts to reestablish connection
#         checkpoint = connection.status()
#         print("Connection status is: ", checkpoint)

#     time.sleep(0.5)