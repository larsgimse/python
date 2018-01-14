Some code to find out how to use TwitterAPI and locations filter.

<pre>
r = api.request('statuses/filter', {'locations':'-74,40,-73,41'}) #NYC 
for item in r:
        print(item)
</pre>

<img src="https://github.com/larsgimse/python/blob/master/twitter/BBox_oslo.png" width=400>
http://boundingbox.klokantech.com/

Oslo: api.request('statuses/filter', {'locations':'10.577063,59.831563,10.90116,59.994724'})

Python code: https://github.com/larsgimse/python/blob/master/twitter/twitter_oslo.py
