import os                                                                                                                                               
import urllib                                                                                                                                           
import json                                                                                                                                             
import unicodedata                                                                                                                                      
import operator                                                                                                                                         
from google.appengine.api import urlfetch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                        
def youtubereq(youtubeid):
    url = "http://gdata.youtube.com/feeds/api/users/" + youtubeid + "/uploads?v=2&alt=jsonc&max-results=5"                                                                                                                                         
    response = urlfetch.fetch(url, headers={'Content-Type': 'application/json'}) 
    content = json.loads(response.content.decode('utf8'))
    return content

#Help