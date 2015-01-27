import os
import urllib
import json
import unicodedata
import operator
from google.appengine.api import urlfetch


# Get the feed
URL = "http://gdata.youtube.com/feeds/api/users/" + 
content = urllib.urlopen(URL).read()
result = json.loads(content)["data"]["items"]

 
# Loop through the result.
for item in result:
 
    print "Video Title: %s" % (item['title'])
 
    print "Video Category: %s" % (item['category'])
 
    print "Video ID: %s" % (item['id'])
 
    print "Video Rating: %f" % (item['rating'])
 
    print "Embed URL: %s" % (item['player']['default'])
    
def youtubereq(url, youtubeid):

    response = urlfetch.fetch(url)
    return response