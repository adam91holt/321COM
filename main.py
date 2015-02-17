from google.appengine.api import users
from google.appengine.ext import db
import webapp2
import jinja2
import urllib
import urllib2
import json
import os
import unicodedata
import operator
from google.appengine.api import urlfetch
import oauth2 as oauth
import logging

#Modles we have made
import twitterreq, teams, teamsForDatastore, youtubemodule 

#Adds all teams to datastore from teamsForDatstore module
teamsForDatastore.dataStoreTeams()


#Set jinja environment so we can pass through data to html
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')),
    extensions=['jinja2.ext.autoescape'])
	
    
#Will be used as the main part of the app
class TeamList(webapp2.RequestHandler):
    def get(self):
        
        #Gets all teams from datastore
        query = db.GqlQuery("SELECT * FROM Team")
        
        #Matches teams to datastore and puts them in position
        allteams = teams.tableStandings()
        
        #Pass all values and create the template
        template = JINJA_ENVIRONMENT.get_template('index.html')
        template_values = {
            'query': query,
            'allteams': allteams,
        }
        self.response.write(template.render(template_values))

        
class TeamData(webapp2.RequestHandler):
    def get(self):
        
        #ADAMS BIT
        
        #Argument - gets the team from the url that is passes
        arg = self.request.get('team')
        #Gets all the players using teams.py
        teamPlayers = teams.teamList(arg)
        
        #Get the team from datastore where the team name is = the team that was passed through url
        query = db.GqlQuery("SELECT * FROM Team WHERE teamName IN ('" + arg + "')")
        
        #Abbas's Bit
        
        #Pass through the team name to the youtube module
        youtube = youtubemodule.youtubereq(query[0].youtube)

        
        #REISS' BIT
        
        #url for twittertest
        #Put team name in URL below for the Twitter request. 
        #gotta take away the @ symbol
        minusfirst = query[0].twitter[1:]
        #twitter url, change the count to get more results
        twitterurl = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + minusfirst +"&count=10"
        #not really neded parameters mostly for put operations will take this out when cleaning up
        parameters = []
        #will store the formated tweets, again this can be seriously cleaned up
        tweets = []
        response = twitterreq.twitterreq(twitterurl, "GET", parameters)
        #stops all the tweets coming out in complete unreadable jargon
        content = json.loads(response.content.decode('utf8'))
        for item in content:
        #just a test format, this can change
            #tweets.append('<h1>' + item['user']['name'] +'</h1>\n' +'<p>' + item['text'] +'</p>\n')
            tweets.append(item)
            
            
        #Create template for the page with the values
        template = JINJA_ENVIRONMENT.get_template('team.html')
        template_values = {
            'players': teamPlayers,
            'tweets': tweets,
            'query': query,
            'youtube': youtube["data"]["items"],
        }
        self.response.write(template.render(template_values))
    
    
    

app = webapp2.WSGIApplication([ 
	('/', TeamList),
    ('/team', TeamData),
	], debug=True)