import os                                                                                                                                               
import urllib                                                                                                                                           
import json                                                                                                                                             
import unicodedata                                                                                                                                      
import operator                                                                                                                                         
from google.appengine.api import urlfetch                                                                                                               
                                                                                                                                                        
                                                                                                                                                        
# Get the feed                                                                                                                                                                                                                                                             
# result = json.loads(content)["data"]["items"]                                                                                                           
                                                                                                                                                        
                                                                                                                                                        
# Loop through the result.                                                                                                                              
# for item in result:                                                                                                                                     
                                                                                                                                                        
#     print "Video Title: %s" % (item['title'])                                                                                                           
                                                                                                                                                        
#     print "Video Category: %s" % (item['category'])                                                                                                     
                                                                                                                                                        
#     print "Video ID: %s" % (item['id'])                                                                                                                 
                                                                                                                                                        
#     print "Video Rating: %f" % (item['rating'])                                                                                                         
                                                                                                                                                        
#     print "Embed URL: %s" % (item['player']['default'])                                                                                                 
                                                                                                                                                        
def youtubereq(youtubeid):
    url = "http://gdata.youtube.com/feeds/api/users/" + youtubeid + "/uploads?v=2&alt=jsonc"                                                                                                                                         
    response = urlfetch.fetch(url, headers={'Content-Type': 'application/json'})                                                                                                                      
    return response