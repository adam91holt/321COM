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
	
#For twitter api testing testing purposes
class twittertest(webapp2.RequestHandler):
    def get(self):
        #url for twittertest
        twitterurl = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=avfcofficial&count=1"
        parameters = []
        tweets = []
        response = twitterreq.twitterreq(twitterurl, "GET", parameters)
        content = json.loads(response.content.decode('utf8'))
        for item in content:
            self.response.write(response.content)
        
#This basically is the model of the data that is entered into the datastore
class Team(db.Model):
    teamName = db.StringProperty()
    twitter = db.StringProperty()
    youtube = db.StringProperty()
    lon = db.FloatProperty()
    lat = db.FloatProperty()
    stadium = db.StringProperty()
    emblem = db.StringProperty()

#Add all 20 teams but not wolverhampton like reiss did
Team(key_name='Chelsea', teamName='Chelsea', twitter='@chelseafc', youtube='chelseafc', lon= -0.192541, lat= 51.482505, stadium='Stamford Bridge', emblem = 'http://upload.wikimedia.org/wikipedia/de/5/5c/Chelsea_crest.svg').put()
Team(key_name='ManCity', teamName='Manchester City', twitter='@MCFC', youtube='mcfcofficial', lon= -2.200459, lat=53.483087, stadium='Etihad Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/f/fd/ManCity.svg').put()
Team(key_name='Southampton', teamName='Southampton', twitter='@SouthamptonFC', youtube='theofficialsaints', lon= -1.390984, lat=50.906178, stadium='St Mary\'s Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/c/c9/FC_Southampton.svg').put()
Team(key_name='ManU', teamName='Manchester United', twitter='@ManUtd', youtube='FullTimeDevils', lon= -2.291297, lat=53.463021, stadium='Old Trafford', emblem = 'http://upload.wikimedia.org/wikipedia/de/d/da/Manchester_United_FC.svg').put()
Team(key_name='Arsenal', teamName='Arsenal', twitter='@arsenal', youtube='ArsenalTour', lon= 0.108558899999934510, lat=51.554947700000010000, stadium='The Emirates', emblem = 'http://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg').put()
Team(key_name='Tottenham', teamName='Tottenham Hotspur', twitter='@SpursOfficial', youtube='spursofficial', lon= -0.066430, lat=51.603278, stadium='White Hart Lane', emblem = 'http://upload.wikimedia.org/wikipedia/de/b/b4/Tottenham_Hotspur.svg').put()
Team(key_name='West Ham', teamName='West Ham United', twitter='@whufc_official', youtube='UCCNOsmurvpEit9paBOzWtUg', lon=0.039273, lat=51.532024, stadium='Boleyn Ground', emblem = 'http://upload.wikimedia.org/wikipedia/de/e/e0/West_Ham_United_FC.svg').put()
Team(key_name='Liverpool', teamName='Liverpool', twitter='@LFC', youtube='LiverpoolFC', lon= -2.960873, lat=53.430995, stadium='Anfield', emblem = 'http://upload.wikimedia.org/wikipedia/de/0/0a/FC_Liverpool.svg').put()
Team(key_name='Swansea', teamName='Swansea City', twitter='@SwansOfficial', youtube='SWANSPLAYER', lon= -3.935264, lat=51.642737, stadium='Liberty Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/a/ab/Swansea_City_Logo.svg').put()
Team(key_name='Stoke', teamName='Stoke City', twitter='@stokecity', youtube='UCmFPjHUFr0hyE6eFGvCm7IA', lon= -2.175507, lat=52.988329, stadium='Britannia Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/a/a3/Stoke_City.svg').put()
Team(key_name='Newcastle', teamName='Newcastle United', twitter='@NUFC', youtube='NUFCOfficial1892', lon= -1.621667, lat=54.975593, stadium='St James\' Park', emblem = 'http://upload.wikimedia.org/wikipedia/de/5/56/Newcastle_United_Logo.svg').put()
Team(key_name='Everton', teamName='Everton', twitter='@Everton', youtube='OfficialEverton', lon= -2.966448, lat=53.438979, stadium='Goodison Park', emblem = 'http://upload.wikimedia.org/wikipedia/de/f/f9/Everton_FC.svg').put()
Team(key_name='Crystal', teamName='Crystal Palace', twitter='@CPFC', youtube='OfficialCPFC', lon= -0.085657, lat=51.398347, stadium='Selhurst Park', emblem = 'http://upload.wikimedia.org/wikipedia/de/b/bf/Crystal_Palace_F.C._logo_(2013).png').put()
Team(key_name='West Bromwich', teamName='West Bromwich Albion', twitter='@WBAFCofficial', youtube='OfficialAlbion', lon= -1.964002, lat=52.509599, stadium='The Hawthorns', emblem = 'http://upload.wikimedia.org/wikipedia/de/8/8b/West_Bromwich_Albion.svg').put()
Team(key_name='Sunderland', teamName='Sunderland', twitter='@SunderlandAFC', youtube='sunderlandafc', lon= -1.388500, lat=54.914623, stadium='Stadium of Light', emblem = 'http://upload.wikimedia.org/wikipedia/de/6/60/AFC_Sunderland.svg').put()
Team(key_name='Villa', teamName='Aston Villa', twitter='@avfcofficial', youtube='avfcofficial', lon= -1.8862340000000586, lat=52.510129, stadium='Villa Park', emblem = 'http://upload.wikimedia.org/wikipedia/de/9/9f/Aston_Villa_logo.svg').put()
Team(key_name='Burnley', teamName='Burnley', twitter='@BurnleyOfficial', youtube='officialburnleyfc', lon= -2.230209, lat=53.788947, stadium='Turf Moor', emblem = 'http://upload.wikimedia.org/wikipedia/de/8/87/Burnley_FC.gif').put()
Team(key_name='Hull', teamName='Hull City', twitter='@HullFCNews', youtube='HCAFCOfficial', lon= -0.367735, lat=53.746560, stadium='KC Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/a/a9/Hull_City_AFC.svg').put()
Team(key_name='QPR', teamName='Queens Park Rangers', twitter='@QPRFC', youtube='OfficialQPR', lon= -0.232914, lat=51.509689, stadium='Loftus Road', emblem = 'http://upload.wikimedia.org/wikipedia/de/d/d4/Queens_Park_Rangers.svg').put()
Team(key_name='Leicester', teamName='Leicester City', twitter='@OfficialFOXES', youtube='LCFCOfficial', lon= -1.141543, lat=52.620109, stadium='King Power Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/en/6/63/Leicester02.png').put()




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
            'allteams': allteams,
        	}
        	self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
    def post(self):
        #Not being used at the moment!!!!!
        self.redirect('/' + urllib.urlencode(query_params))
        
class TeamData(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        #Actual API request
        data = urllib2.urlopen('http://api.football-data.org/alpha/soccerseasons/354/leagueTable').read()
        #Decode to JSON                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        dataDecode = json.loads(data.decode('utf8'))    
        #Store all teams
        teamlist = dataDecode['standing']
        #Argument - this will later be passed in via URL
        arg = self.request.get('team')
        #get the query from the url
        query = db.GqlQuery("SELECT * FROM Team WHERE teamName IN ('" + arg + "')")
        # these work just like console logging in javascript enjoy! they will appear in the terminal
        # logging.info(whatever variable/string) 
        # query[0] will be the single team for each page so you can choose its attributes from that
        # _____________________________________________________________
        #Array to store all players in... will be store in tuples
        teamPlayers = []
        #For loops to search all teams with arguement and then get players into the teamPlayers array
        for t in teamlist:
            #Get each club name
            club = t['teamName']
            #Finds the team from the one that was passed throuh
            if arg in club:
                #Get the url for the club
                cluburl = t['_links']['team']['href']
                #Open up the url
                openclub = urllib2.urlopen(cluburl).read()
                #Convert JSON
                clubJSON = json.loads(openclub.decode('utf8')) 
                #Players URL
                playersurl = clubJSON['_links']['players']['href']
                #Get all players
                openplayers = urllib2.urlopen(playersurl).read()
                #Convert JSON
                players = json.loads(openplayers.decode('utf8'))
                #Variable for all the players
                player = players['players']
                for p in player:
                    person = (p['jerseryNumber'], p['name'], p['position'])
                    teamPlayers.append(person)
        
        #url for twittertest
        #Put team name in URL below for the Twitter request. 
        #gotta take away the @ symbol
        minusfirst = query[0].twitter[1:]
        #twitter url, change the count to get more results
        twitterurl = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + minusfirst +"&count=10"
        #not really neded parameters mostly for put operations will take this out when cleaning up
        parameters = []
#       will store the formated tweets, again this can be seriously cleaned up
        tweets = []
        response = twitterreq.twitterreq(twitterurl, "GET", parameters)
#         stops all the tweets coming out in complete unreadable jargon
        content = json.loads(response.content.decode('utf8'))
        for item in content:
        #just a test format, this can change
            #tweets.append('<h1>' + item['user']['name'] +'</h1>\n' +'<p>' + item['text'] +'</p>\n')
            tweets.append(item)
        #Pass in all templated if user is logged in
        if user:
        	template = JINJA_ENVIRONMENT.get_template('team.html')
        	template_values = {
                'user': user.nickname(),
                'url_logout': logout_url,
                'url_logout_text': 'Log out',
                'players': teamPlayers,
                'tweets': tweets,
                'query': query,
        	}
        	self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
        

app = webapp2.WSGIApplication([ 
	('/', TeamList),
    ('/team', TeamData),
    ('/twittertest', twittertest),
	], debug=True)