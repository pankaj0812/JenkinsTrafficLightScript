import json
import sys
import urllib2
import time
import serial
import base64
# Configurations
ping_server = 30
jenkins_jobs = ["Test"]
ser = serial.Serial('COM12', 9600)
# Arduino Configurations
SUCCESS = 'b'
FAILURE = 'r'
BUILDING = 'a'
UNSTABLE = 'y'

user = "lucifer"
password = ""

time.sleep(5)
def get_status(jobName, data=None):
    jenkinsUrl = "http://localhost:8080/job/" + jobName + "/lastBuild/api/json"
    request = urllib2.Request(jenkinsUrl, data)
    base64string = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    jenkinsStream = urllib2.urlopen(request)
    # print jenkinsStream.read()
    # try:
    #     jenkinsStream = urllib2.urlopen(request)
    #     # print jenkinsStream.read()
    # except urllib2.HTTPError, e:
    #     print "URL Error: "+str(e.code)
    #     print "job name [" +jobName + "] probably Wrong"
    #     sys.exit(2)
    try:
        buildStatusJson = json.load(jenkinsStream)
        print buildStatusJson.has_key("result")
    except:
        print "Failed to parse json"
        sys.exit(3)
    return jobName, buildStatusJson["timestamp"], buildStatusJson["result"]


while(1):
    for job in jenkins_jobs:
        status = get_status(job)
        print status[0], status[2]
        if status[2] == "UNSTABLE":
            ser.write(UNSTABLE)
        elif status[2] == "SUCCESS":
            ser.write(SUCCESS)
        elif status[2] == "FAILURE":
            ser.write(FAILURE)
        elif status[2] == "None":
            ser.write(BUILDING)
        time.sleep(ping_server)




