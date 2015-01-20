# import urllib2
# import json
# import os
# import unicodedata
# import operator
# from google.appengine.api import urlfetch
# import oauth2 as oauth
# import logging
# import twitterreq
# # # # set up the access tokens for twitter ap# i
# access_token_key = "2987158727-iO2hbvb1ZTsTzBhsRaWiJeVweOGszeGg8QV0DIf"
# access_token_secret = "yGaZ2rIlXhZWJIa9kHrUTKHm39eAWg6nCd93g6Lpot9FR"
# consumer_key = "AltdPvTrRMGYc0M87xqcGVGk4"
# consumer_secret = "TGePRJfLFol3PERwul5RgD1mBybsA3v8Y1SPiTSIG1Nm7REbVF"


# _debug = 0

# oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
# oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

# signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

# http_method = "GET"

# http_handler = urllib2.HTTPHandler(debuglevel=_debug)
# https_handler = urllib2.HTTPSHandler(debuglevel=_debug)

# ##define the twitter request method
# def twitterreq(url, method):
#     req = oauth.Request.from_consumer_and_token(oauth_consumer,
#                                              token=oauth_token,
#                                              http_method=http_method,
#                                              http_url=url)
#     req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
#     headers = req.to_header()
#     if http_method == "POST":
#         encoded_post_data = req.to_postdata()
#     else:
#         encoded_post_data = None
#     url = req.to_url()

#     opener = urllib.OpenerDirector()
#     opener.add_handler(http_handler)
#     opener.add_handler(https_handler)
#     logging.info(req)
#     #response = opener.open(url, encoded_post_data)
#     #response = urlfetch.fetch(url)
#     response = urlfetch.fetch(url)
#     print headers
#     return response
#     
#     
#     
import os
import oauth2 as oauth
import urllib
import json
import unicodedata
import operator
from google.appengine.api import urlfetch

#You need to sign up and create an application at https://dev.twitter.com/apps
#to create the access_token_key, access_token_secret, consumer key and consumer secret

access_token_key = "2987158727-iO2hbvb1ZTsTzBhsRaWiJeVweOGszeGg8QV0DIf"
access_token_secret = "yGaZ2rIlXhZWJIa9kHrUTKHm39eAWg6nCd93g6Lpot9FR"
consumer_key = "AltdPvTrRMGYc0M87xqcGVGk4"
consumer_secret = "TGePRJfLFol3PERwul5RgD1mBybsA3v8Y1SPiTSIG1Nm7REbVF"


_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


#http_handler  = urllib.HTTPHandler(debuglevel=_debug)
#https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method,parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)
    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
    headers = req.to_header()
    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
    url = req.to_url()

    #opener = urllib.OpenerDirector()
    #opener.add_handler(http_handler)
    #opener.add_handler(https_handler)

    response = urlfetch.fetch(url, encoded_post_data)
    return response