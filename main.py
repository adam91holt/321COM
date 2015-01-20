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
import twitterreq







#Set jinja environment so we can pass through data to html
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')),
    extensions=['jinja2.ext.autoescape'])
	
#For testing purposes
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('hello')
        self.response.write('test')
        #url for twittertest
        twitterurl = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=2"
        parameters = []
        tweets = []
        response = twitterreq.twitterreq(twitterurl, "GET", parameters)
        logging.info(response.content)
        content = response.content
        test = content.split(',')
        self.response.write(content)
        self.response.write(len(test))
        for item in test:
            self.response.write('item:' + item)
        
#This basically is the model of the data that is entered into the datastore
class Team(db.Model):
    teamName = db.StringProperty()
    twitter = db.StringProperty()
    youtube = db.StringProperty()
    lon = db.FloatProperty()
    lat = db.FloatProperty()
    stadium = db.StringProperty()
    emblem = db.StringProperty()

#Add all 20 teams
Team(key_name='Arsenal', teamName='Arsenal', twitter='@arsenal', youtube='ArsenalTour', lon=0.108558899999934510, lat=51.554947700000010000, stadium='The Emirates', emblem = 'http://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg').put()
Team(key_name='Villa', teamName='Aston Villa', twitter='@avfcofficial', youtube='avfcofficial', lon=-1.8862340000000586, lat=52.510129, stadium='Villa Park', emblem = 'http://upload.wikimedia.org/wikipedia/de/9/9f/Aston_Villa_logo.svg').put()



#Will be used as the main part of the app
class TeamList(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
#         query = db.GqlQuery("SELECT * FROM Team WHERE teamName IN ('Arsenal')")
        query = db.GqlQuery("SELECT * FROM Team")
        logout_url = users.create_logout_url(self.request.path)
        

        #URL for getting all teams     
        #urllib2.urlopen                                                                                                                                                                                                                         
        data = urllib2.urlopen('http://api.football-data.org/alpha/soccerseasons/354/leagueTable').read()
        #Variables to get to where is needed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        dataDecode = json.loads(data.decode('utf8'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        teamlist = dataDecode['standing']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        #Stores all teams and positions
        allteams = []
        #For loop to get all necessary values
        for team in teamlist:
            t = (str(team['teamName']), team['position'])
            allteams.append(t)
        #End Loop
        
        #Pass in all templated if user is logged in
        if user:
        	template = JINJA_ENVIRONMENT.get_template('index.html')
        	template_values = {
            'user': user.nickname(),
            'url_logout': logout_url,
            'url_logout_text': 'Log out',
            'query': query,
            'data': data,
            'allteams': allteams,
        	}
        	self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
    def post(self):
        #Not being used at the moment!!!!!
        self.redirect('/' + urllib.urlencode(query_params))
        
    

app = webapp2.WSGIApplication([ 
	('/', TeamList),
    ('/team',TeamList),
	], debug=True)