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
        #url for twittertest
        twitterurl = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=chelseafc&count=5"
        parameters = []
        tweets = []
        response = twitterreq.twitterreq(twitterurl, "GET", parameters)
        content = json.loads(response.content.decode('utf8'))
        for item in content:
            self.response.write('<h1>' +item['user']['name'] +'</h1>\n')
            self.response.write('<p>'+ item['text'] +'</p>\n')
        
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
Team(key_name='Chelsea', teamName='Chelsea FC', twitter='@chelseafc', youtube='chelseafc', lon=-0.190941, lat=51.481705, stadium='Stamford Bridge', emblem = 'http://upload.wikimedia.org/wikipedia/de/5/5c/Chelsea_crest.svg').put()
Team(key_name='ManCity', teamName='Manchester City FC', twitter='@MCFC', youtube='mcfcofficial', lon=-2.200459, lat=53.483087, stadium='Etihad Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/f/fd/ManCity.svg').put()
Team(key_name='Southampton', teamName='FC Southampton', twitter='@SouthamptonFC', youtube='theofficialsaints', lon=-1.390984, lat=50.906178, stadium='St Mary\'s Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/c/c9/FC_Southampton.svg').put()
Team(key_name='ManU', teamName='Manchester United FC', twitter='@ManUtd', youtube='FullTimeDevils', lon=-2.291297, lat=53.463021, stadium='Old Trafford', emblem = 'http://upload.wikimedia.org/wikipedia/de/d/da/Manchester_United_FC.svg').put()
Team(key_name='Arsenal', teamName='Arsenal', twitter='@arsenal', youtube='ArsenalTour', lon=0.108558899999934510, lat=51.554947700000010000, stadium='The Emirates', emblem = 'http://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg').put()
Team(key_name='Tottenham', teamName='Tottenham Hotspur FC', twitter='@SpursOfficial', youtube='spursofficial', lon=-0.066430, lat=51.603278, stadium='White Hart Lane', emblem = 'http://upload.wikimedia.org/wikipedia/de/b/b4/Tottenham_Hotspur.svg').put()
Team(key_name='West Ham', teamName='West Ham United FC', twitter='@whufc_official', youtube='UCCNOsmurvpEit9paBOzWtUg', lon=0.039273, lat=51.532024, stadium='Boleyn Ground', emblem = 'http://upload.wikimedia.org/wikipedia/de/e/e0/West_Ham_United_FC.svg').put()
Team(key_name='Liverpool', teamName='Liverpool FC', twitter='@LFC', youtube='LiverpoolFC', lon=-2.960873, lat=53.430995, stadium='Anfield', emblem = 'http://upload.wikimedia.org/wikipedia/de/0/0a/FC_Liverpool.svg').put()
Team(key_name='Swansea', teamName='Swansea City', twitter='@SwansOfficial', youtube='SWANSPLAYER', lon=-3.935264, lat=51.642737, stadium='Liberty Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/a/ab/Swansea_City_Logo.svg').put()
Team(key_name='Stoke', teamName='Stoke City FC', twitter='@stokecity', youtube='UCmFPjHUFr0hyE6eFGvCm7IA', lon=-2.175507, lat=52.988329, stadium='Britannia Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/a/a3/Stoke_City.svg').put()
Team(key_name='Everton', teamName='Everton FC', twitter='@Everton', youtube='OfficialEverton', lon=-2.966448, lat=53.438979, stadium='Goodison Park', emblem = 'http://upload.wikimedia.org/wikipedia/de/f/f9/Everton_FC.svg').put()
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
    ('/twittertest',MainHandler),
	], debug=True)