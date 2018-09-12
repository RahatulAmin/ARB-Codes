import serial
import os
import glob
import subprocess
import calendar
import time
import urllib2
import json

ser = serial.Serial("/dev/ttyACM0",9600)

saveFile = open('DataFile.txt','w')

while 1:
        read=ser.readline()
#	parameters = read.split(",")
 #       print("Voltage: " + parameters[0])
#	print("pH Value: " + parameters[1])
#	print("Temperature: " + parameters[2])
#	print("Global Position: " + parameters[3])
	print read
	saveFile.write(read) 
     #  saveFile.write(parameters[0])
#	saveFile.write(parameters[1])
#	saveFile.write(parameters[2])
#	saveFile.write(parameters[3])
	
saveFile.close()

