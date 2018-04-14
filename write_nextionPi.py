
import serial
txt="test text"

ser = serial.Serial(
  port='/dev/ttyAMA0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

EndCom = "\xff\xff\xff"
ser.write('page1.t0.txt=txt'+EndCom)
