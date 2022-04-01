import serial
"""
    Positioning module
    ---
    Geolocation using gps module
    view https://www.sparkfun.com/tutorials/403 for more information
    https://maker.pro/raspberry-pi/tutorial/how-to-read-gps-data-with-python-on-a-raspberry-pi
"""
def init_serial():
    COMNUM = 9 # set your COM PORT HERE
    global ser # must be declared in each fxn used
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = COMNUM - 1 # starts at 0, so subtract 1
    # ser.port = '/dev/ttyUSB0' # uncomment for linux 

    # you must specify a timeout (in seconds) so that the
    # serial port doesn't hang
    ser.timeout = 1
    ser.open() #open the serial port
    if ser.isOpen():
        print('Open: ' + ser.portstr)