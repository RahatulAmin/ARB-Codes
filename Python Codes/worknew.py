__author__ = 'skunda'
# This program logs a Raspberry Pi's CPU temperature to a Thingspeak Channel
# To use, get a Thingspeak.com account, set up a channel, and capture the Channel Key at https://thingspeak.com/docs/tutorials/ 
# Then paste your channel ID in the code for the value of "key" below.
# Then run as sudo python pitemp.py (access to the CPU temp requires sudo access)
# You can see my channel at https://thingspeak.com/channels/41518

import httplib, urllib
import time
sleep = 3 # how many seconds to sleep between posts to the channel
key = '3004Z6NY6N23TADR'  # Thingspeak channel to update

#Report Raspberry Pi internal temperature to Thingspeak Channel
def thermometer():
    #while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
    temp = open('/home/pi/graph.txt','r').read() # Get Raspberry Pi CPU temp
    readings = temp.split(",")
        #line = 0
    for line in range(0,len(readings),2):
        #for line in range(len(readings)):
        var=line+1
        params = urllib.urlencode({'field6': readings[line], 'field7': readings[var], 'key':key }) 
            #params = urllib.urlencode({'field6': readings[line], 'key':key }) 

        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
                #print temp
            print readings[line]
            print readings[var]
            #print int(readings[line])
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        #break
#sleep for desired amount of time
if __name__ == "__main__":
        #while True:
                #thermometer()
                #time.sleep(sleep)
        thermometer()
