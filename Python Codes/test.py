import serial
import os
import glob
import subprocess
import calendar
import time
import urllib2
import json

ser = serial.Serial("/dev/ttyACM3",9600)

saveFile = open('testfile.txt','w')

while 1:
        read=ser.readline()
#	parameters = read.split(",")
        print read
#	url = "https://aqua-research-bot-9033b.firebaseio.com/readings.json"

#	req = urllib2.Request(url)
#	req.add_header('Content-Type','application/json')
#	data = json.dumps(postdata)
	
#	response = urllib2.urlopen(req,data)
	
        saveFile.write(read)
	saveFile.write('\n\n')
	
saveFile.close()

