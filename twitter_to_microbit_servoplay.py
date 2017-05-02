# -*- coding: utf-8 -*-
# Author: Nicholas Bester (Arduino)
# reAuthor to micro:bit: Lars Gisme
# Title: Twitter Stream connection with micro:bit
# Description: Tracks a string using the Twitter API and sends a Serial command to an micro:bit once a Tweet matching the tracked string is found


# imports
import time
from time import sleep
from TwitterAPI import TwitterAPI
import struct
import os
from serial import Serial
import httplib
from httplib import IncompleteRead
import random
from random import randint

availableMicrobit = True # Debugging without an micro:bit
testSerial = True # Debugging without Twitter connection
microbitPort = '/dev/ttyACM0' # USB port address for the micro:bit /dev/tty.usbmodem1412
microbitBaud = '115200' # Baud for serial communication
microbitWaitTime = 1 # The length of time Python wait before attemping to issue commands to the micro:bit
stringToTrack = "#romforlek" # Change this to the search term you wish to track from Twitter
servoTime= 10
vinkel = 73

from auth_romforlek import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

servoAngle = ('0',
              '45',
              '90',
              '135',
              '180')

os.system('cls' if os.name == 'nt' else 'clear')

print "Initialising Twitter Stream Application"

print "Initialisation OK!"

print 'Initialising micro:bit Board through Serial'


if availableMicrobit:
  ser = Serial(microbitPort, microbitBaud, timeout=3)

sleep(microbitWaitTime)

if testSerial:
  for x in range(0,10):
    angleSet = random.choice(servoAngle)
    ser.write(angleSet)
    sleep(1)
    print(x)
    print(angleSet)
    print '----'
    (x)

else:
  print "Initialisation OK!"
  print 'Initialising Twitter Stream API Authorisation'
  try:
    api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

    print "Initialisation OK!"
    print 'Twitter Stream Request running'

    r = api.request('statuses/filter', {'track':stringToTrack})

    for item in r.get_iterator():
      if 'text' in item:
        print item['user']['screen_name'].encode('utf-8') + ' tweeted: ' + item['text'].encode('utf-8')# Print screen name and the tweet text
        tweet = item['text'].encode('utf-8')
        print tweet.split()
        if '#servo0' in tweet.split():
                print 'Send servo 0 til micro:bit'
                ser.write('0')
                sleep(servoTime)
        elif '#servo180' in tweet.split():
                print 'Send servo 180 til micro:bit'
                ser.write('180')
                sleep(servoTime)
        elif '#servo90' in tweet.split():
                print 'Send servo 90 til micro:bit'
                ser.write('90')
                sleep(servoTime)
        elif '#servo45' in tweet.split():
                print 'Send servo 45 til micro:bit'
                ser.write('45')
                sleep(servoTime)
        elif '#servo135' in tweet.split():
                print 'Send servo 135 til micro:bit'
                ser.write('135')
                sleep(servoTime)
        elif '#servoplay' in tweet.split():
          for x in range(0,10):
            angleSet = random.choice(servoAngle)
            ser.write(angleSet)
            sleep(1)
            print(x)
            print(angleSet)
            print '----'
            (x)
                
  except IncompleteRead:
    print "IncompleteRead occurred"
  except KeyboardInterrupt:
    api.disconnect()
    exit()
