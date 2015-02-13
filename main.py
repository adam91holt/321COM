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
<<<<<<< HEAD
import twitterreq
import youtubemodule
=======
>>>>>>> 609784f0760cc9acec7ac841b61e68ea2264f883

#Modles we have made
import twitterreq, teams, teamsForDatastore 



#Adds all teams to datastore from teamsForDatstore module
teamsForDatastore.dataStoreTeams()


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
        

#Will be used as the main part of the app
class TeamList(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
        
        #Gets all teams from datastore
        query = db.GqlQuery("SELECT * FROM Team")
        
        #Matches teams to datastore and puts them in position
        allteams = teams.tableStandings()
        
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


        # these work just like console logging in javascript enjoy! they will appear in the terminal
        # logging.info(whatever variable/string) 
        # query[0] will be the single team for each page so you can choose its attributes from that
        # _____________________________________________________________
        
        #ADAMS BIT
        
        #Argument - gets the team from the url that is passes
        arg = self.request.get('team')
        #Gets all the players using teams.py
        teamPlayers = teams.teamList(arg)
        
        #Get the team from datastore where the team name is = the team that was passed through url
        query = db.GqlQuery("SELECT * FROM Team WHERE teamName IN ('" + arg + "')")
<<<<<<< HEAD
        # these work just like console logging in javascript enjoy! they will appear in the terminal 
        logging.info(query[0].twitter)
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
        youtube = youtubemodule.youtubereq(query[0].youtube)
=======
        
        #REISS' BIT
        
        #url for twittertest
        #Put team name in URL below for the Twitter request. 
        #gotta take away the @ symbol
>>>>>>> 609784f0760cc9acec7ac841b61e68ea2264f883
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
<<<<<<< HEAD
            'user': user.nickname(),
            'url_logout': logout_url,
            'url_logout_text': 'Log out',
            'players': teamPlayers,
            'tweets': tweets,
            'youtube': youtube,
=======
                'user': user.nickname(),
                'url_logout': logout_url,
                'url_logout_text': 'Log out',
                'players': teamPlayers,
                'tweets': tweets,
                'query': query,
>>>>>>> 609784f0760cc9acec7ac841b61e68ea2264f883
        	}
        	self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            

API_KEY = "AIzaSyBZB23pzOwqTekDeTes4ZyLg4Pr2DGUp1U"

        
# Youtube test module       
class youtubetest(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
#         The response holds the data collected from the api
        response = youtubemodule.youtubereq("chelseafc")
#      
        if user:
        	template = JINJA_ENVIRONMENT.get_template('youtube.html')
        	template_values = {
            'youtube': response["data"]["items"],
        	}
        	self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    
    
    

app = webapp2.WSGIApplication([ 
	('/', TeamList),
<<<<<<< HEAD
    ('/team',TeamData),
    ('/twittertest',MainHandler),
    ('/youtube', youtubetest),
=======
    ('/team', TeamData),
    ('/twittertest', twittertest),
>>>>>>> 609784f0760cc9acec7ac841b61e68ea2264f883
	], debug=True)