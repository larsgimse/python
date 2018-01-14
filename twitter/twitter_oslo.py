# -*- coding: utf-8 -*-

from TwitterAPI import TwitterAPI

from auth_romforlek import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

tweet_number = 0

api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
print 'Twitter ready!'

r = api.request('statuses/filter', {'locations':'10.577063,59.831563,10.90116,59.994724'})

for item in r:
        tweet_number = tweet_number + 1
        tweet_user = item['user']['screen_name'].encode('utf-8')
        tweet = item['text'].encode('utf-8')
        tweet_place = item['place']['full_name']

        print tweet_number
        print tweet_user
        print tweet
        print tweet_place

        print("--------")
        print("")
