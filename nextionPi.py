#import modules
import serial
#Set end of file
eof = "\xff\xff\xff"

#setup connection
ser = serial.Serial(

    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

#loop waiting for hex input
while 1:
    #get the data from the nextion display
    x = ser.readline()
    #print output with repr (returns a string containing a printable representation of an object)
    print "Recieved:" + repr(x)
