#rough code for ODB setup
#Jackson + Marcus
#2/27/22
"""
OBD Module
----------
Functions as connectivity between the HUD and OBDII bluetooth transmitter.
Establishes a connection to the bluetooth adapter and gathers measurements such
as speed and fuel percentage. When it first forms a connection the code has to
loop multiple times to pull all instructions.
"""
import obd
from obd import OBDStatus as status
import time
import threading

#Attempt to establish a connection and initialize a timer to keep track of wait cycles.
class Obd(threading.Thread):
    def __init__(self, display):
        threading.Thread.__init__(self) # initialization of thread
        self.checkpoint = "Disconnected"
        obd.logger.setLevel(obd.logging.DEBUG)
        print("Attempting to establish connection")
        #self.connect() # comment this line out if testing locally
        print("Connection formed.")
        print("Connection status is: ", self.checkpoint)
        self.screen = display
        self.speedInKilo = None
        self.fuelPercentage = None

    def connect(self):
        """Forms a connection to the OBDII module. Retries until a certain number of commands
        are available.
        """
        self.connection = obd.OBD(portstr="/dev/rfcomm0", protocol='6', fast=False)
        while (len(self.connection.supported_commands) < 100):
            self.connection = obd.OBD(portstr="/dev/rfcomm0", protocol='6', fast=False)

        self.checkpoint = self.connection.status()

    def get_dtc(self):
        if self.connection.status() == status.CAR_CONNECTED:
            return self.connection.query(obd.commands.DTC)

    def is_healthy_message(dtc):
        if len(dtc) == 0:
            return "Healthy"
        return "Error(s)"


    def get_speed(self):
        """ Queries speed of car is connected
        Returns:
            string: speed in mph
        """

        speed = None

        if self.connection.status() == status.CAR_CONNECTED: #If the car is connected and turned on
            speed = self.connection.query(obd.commands.SPEED) #Queries the speed, object with a value in kilometers per hour.

            if speed is None:
                return "Could not obtain speed"
            else:
                self.speedInKilo = speed
                # in the meantime, print results for debugging purposes
                return self.speedInKilo

    def get_fuel_percentage(self):
        """ Queries fuel % of car is connected 
        Returns:
            string: fuel percentage
        """
        if self.connection.status() == status.CAR_CONNECTED: #If the car is connected and turned on
            self.fuelPercentage = self.connection.query(obd.commands.FUEL_LEVEL).value #Returns a % of fuel
            
        if self.fuelPercentage is None:
            return "Could not pull fuel percentage"
        else:
            return self.fuelPercentage

    def run(self):
        """ While loop that relies on previous functions to show the user what is occuring. """
        count = 0
        while True:
            # uncomment these lines when testing locally
            self.screen.show_obd(count)
            print("OBD is running here...")
            time.sleep(10)
            count = count + 1
            
            # uncomment these lines when using an actual display
            # ==================================================
            # fuel = str(self.get_fuel_percentage())
            # speed = str(self.get_speed())
            # speedstring = "Speed is:" + speed
            # fuelstring = "Fuel percentage is: " + fuel
            # print(speedstring)
            # print(fuelstring)
            # print("Updating...")
            # time.sleep(1)  
