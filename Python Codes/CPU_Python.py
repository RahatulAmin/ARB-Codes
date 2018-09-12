#!/usr/bin/env python
__author__ = 'skunda'
# This program logs a Raspberry Pi's CPU temperature to a Thingspeak Channel
# To use, get a Thingspeak.com account, set up a channel, and capture the Channel Key at https://thingspeak.com/docs/tutorials/ 
# Then paste your channel ID in the code for the value of "key" below.
# Then run as sudo python pitemp.py (access to the CPU temp requires sudo access)
# You can see my channel at https://thingspeak.com/channels/41518
import httplib, urllib
import time
sleep = 2 # how many seconds to sleep between posts to the channel
key = '3004Z6NY6N23TADR' # Thingspeak channel to update

#Report Raspberry Pi internal temperature to Thingspeak Channel

def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        #temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp

        temp = open('/home/pi/graph1.txt','r').read()
        readings = temp.split("\n")
        #val=0
        line = 0
        for line in range(len(readings)):
            params = urllib.urlencode({'field5': int(readings[line]), 'key':key }) 
            #val=val+1
           # params1 = urllib.urlencode({'field5': int(readings[line+val]), 'key':key }) 
           # val=val+1
            headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
            conn = httplib.HTTPConnection("api.thingspeak.com:80")
            try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                print int(readings[line])
                print response.status, response.reason
                data = response.read()
                conn.close()
            except:
                print "connection failed"
            #break
#sleep for desired amount of time
if __name__ == "__main__":
        while True:
                thermometer()
                time.sleep(sleep)

