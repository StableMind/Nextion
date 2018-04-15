
#import module: install with 'easy_install -U pyserial'
import serial

#Set end of file
eof = "\xff\xff\xff"

#setup text for writing
txt = 'Hello wold'

#setup connection
con = serial.Serial(

    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)

#write text to Page 0 t0 txt variable(check the id of your text box) plus EOF
con.write('page0.t0.txt='txt+eof)
