import OBD
from obd import OBDStatus as status

obd = OBD.Obd()
#Attempt to establish a connection and initialize a timer to keep track of wait cycles.
while obd.connection.status() != status.CAR_CONNECTED:
    obd.connect()   #  try reconnect on fail

while obd.connection.status() == status.CAR_CONNECTED:
    fuel = obd.get_fuel_percentage();
    speed = obd.get_speed();
    print("fuel: ", fuel)
    print("speed: ", speed)

