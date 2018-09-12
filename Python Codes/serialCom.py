import serial

ser = serial.Serial("/dev/ttyACM0",9600)

while 1:
	read = ser.readline()
	print read


