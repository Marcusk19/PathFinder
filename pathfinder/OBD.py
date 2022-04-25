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
        self.speedInMiles = 0.00
        self.fuelPercentage = 0.00

        self.connection = obd.OBD(portstr="/dev/rfcomm0", protocol='6', baudrate=38400, fast=False)
        retries = 0
        while (len(self.connection.supported_commands) < 100):
            self.connection = obd.OBD(portstr="/dev/rfcomm0", protocol='6', baudrate=38400, fast=False)
            retries = retries + 1

        if self.connection is not None:
            self.checkpoint = self.connection.status()


    def get_dtc(self):
        if self.connection.status() == status.CAR_CONNECTED:
            return self.connection.query(obd.commands.GET_DTC)

    def is_healthy_message(self, dtc):
        if dtc is None:
            return "Disconnected"
        if len(dtc.value) == 0:
            return "Healthy"
        if len(dtc.value) == 1:
            return dtc.value[0]
        return dtc[0][0]


    def get_speed(self):
        """ Queries speed of car is connected
        Returns:
            string: speed in mph
        """

        speed = None

        if self.connection.status() == status.CAR_CONNECTED: #If the car is connected and turned on
            speed = self.connection.query(obd.commands.SPEED) #Queries the speed, object with a value in kilometers per hour.

            if speed is None:
                return 0.00
            else:
                self.speedInMiles = speed.value.to('mph')
                # in the meantime, print results for debugging purposes
                return int(self.speedInMiles.magnitude)

    def get_fuel_percentage(self):
        """ Queries fuel % of car is connected 
        Returns:
            string: fuel percentage
        """
        if self.connection.status() == status.CAR_CONNECTED: #If the car is connected and turned on
            self.fuelPercentage = self.connection.query(obd.commands.FUEL_LEVEL).value #Returns a % of fuel
            
        if self.fuelPercentage is None:
            return 0.00
        else:
            return int(self.fuelPercentage.magnitude)

    def run(self):
        """ While loop that relies on previous functions to show the user what is occuring. """
        count = 0
        while True:
            # uncomment these lines when testing locally
            dtc_code = self.get_dtc()
            health = self.is_healthy_message(dtc_code)
            self.fuelPercentage = self.get_fuel_percentage()
            self.speedInMiles = self.get_speed()
            self.screen.show_obd(self.speedInMiles, self.fuelPercentage, health)
            print("OBD is running here...")
            time.sleep(0.5)
            
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