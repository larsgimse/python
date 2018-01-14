Some code to find out how to use TwitterAPI and locations filter.
https://github.com/geduldig/TwitterAPI

<pre>
r = api.request('statuses/filter', {'locations':'-74,40,-73,41'}) #NYC 
for item in r:
        print(item)
</pre>

How to find Oslo? I found a great online tool.

<img src="https://github.com/larsgimse/python/blob/master/twitter/BBox_oslo.png" width=400>
http://boundingbox.klokantech.com/

<pre>
Oslo: api.request('statuses/filter', {'locations':'10.577063,59.831563,10.90116,59.994724'})
</pre>

Python code: https://github.com/larsgimse/python/blob/master/twitter/twitter_oslo.py

# next - make e-textils with activity o-meter from locations
