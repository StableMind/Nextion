#import module: install with 'easy_install -U pyserial'
import serial
#Set end of file
eof = "\xff\xff\xff"

#setup connection
con = serial.Serial(

    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    
)

#loop waiting for input from nextion
while True:
    #get the data from the nextion display
    readTxt = con.readline()
    #print output to screen with repr (returns a string containing a printable representation of an object)
    print "Data Recieved:" + repr(readText)
