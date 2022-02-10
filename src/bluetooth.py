import obd
import obd
from obd import OBDStatus as status
import time

#Attempt to establish a connection and initialize a timer to keep track of wait cycles.
print("Attempting to establish connection")
obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD(portstr="/dev/tty.OBDII", fast=False, timeout=40)
checkpoint = connection.status()
print("Connection status is: ", checkpoint)
loopTimer = 0