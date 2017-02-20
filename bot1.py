# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

import sys
import operator

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# create oauth token
#    oauth = OAuth(token['ACCESS_TOKEN'], token['ACCESS_SECRET'], token['CONSUMER_KEY'], token['CONSUMER_SECRET'])


#twitter = Twitter(auth=oauth)
#iterator = twitter.statuses.user_timeline(screen_name = user)

#sorted(tweets,key=operator.itemgetter('retweet_count'))
