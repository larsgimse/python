# -*- coding: utf-8 -*-

import time
from time import sleep
from TwitterAPI import TwitterAPI
import struct
import os
from serial import Serial
import httplib
from httplib import IncompleteRead

from auth_romforlek import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

stringToTrack = ""
tweet_number = 0

api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
print 'Twitter ready!'

#r = api.request('statuses/filter', {'track':stringToTrack})

#for item in r.get_iterator():
#    if 'text' in item:
#        tweet = item['text'].encode('utf-8').strip(stringToTrack)
#        print tweet

#r = api.request('search/tweets', {'q':'pizza'})
#for item in r:
        #print(item)
#        tweet_number = tweet_number + 1
#        print tweet_number
					
#r = api.request('statuses/filter', {'locations':'17,69,18,70'})#-74,40,-73,41
r = api.request('statuses/filter', {'locations':'10.577063,59.831563,10.90116,59.994724'})

for item in r:
        #print(item)
        tweet_number = tweet_number + 1
        print tweet_number
        tweet_user = item['user']['screen_name'].encode('utf-8')#.strip(stringToTrack)
        #tweet_user1 = item['user']
        #tweet = item['text'].encode('utf-8')
        #tweet = item['time_zone'].encode('utf-8')
        tweet_place = item['place']['full_name']#.encode('utf-8')
        #tweet_place1 = item['place']
        #tweet_xx = item['profile_image_url_https'].encode('utf-8')
        print tweet_user
        #print tweet_user1
        print tweet_place
        #print tweet_place1
        #print tweet
        #print tweet_xx
        print("--------")
        print("")
