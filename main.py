from google.appengine.api import users
from google.appengine.ext import db
import webapp2
import jinja2
import urllib
import urllib2
import json
import os

#Set jinja environment so we can pass through data to html
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')),
    extensions=['jinja2.ext.autoescape'])
	
#For testing purposes
class MainHandler(webapp2.RequestHandler):
 	def get(self):
 		self.response.write('hello')
        
#This basically is the model of the data that is entered into the datastore
class Team(db.Model):
    teamName = db.StringProperty()
    twitter = db.StringProperty()
    youtube = db.StringProperty()
    lon = db.FloatProperty()
    lat = db.FloatProperty()
    stadium = db.StringProperty()

#Add all 20 teams
Team(key_name='Arsenal', teamName='Arsenal', twitter='@arsenal', youtube='ArsenalTour', lon=0.108558899999934510, lat=51.554947700000010000, stadium='The Emirates').put()
Team(key_name='Villa', teamName='Aston Villa', twitter='@avfcofficial', youtube='avfcofficial', lon=-1.8862340000000586, lat=52.510129, stadium='Villa Park').put()

    
#Will be used as the main part of the app
class TeamList(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
#         query = db.GqlQuery("SELECT * FROM Team WHERE teamName IN ('Arsenal')")
        query = db.GqlQuery("SELECT * FROM Team")
        logout_url = users.create_logout_url(self.request.path)

        if user:
        	template = JINJA_ENVIRONMENT.get_template('teams.html')
        	template_values = {
            'user': user.nickname(),
            'url_logout': logout_url,
            'url_logout_text': 'Log out',
            'query': query,
        	}
        	self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
    def post(self):
        #Not being used at the moment!!!!!
        datastore_name = self.request.get('datastore_name', 'teams')
        greeting = Greeting(parent=guestbook_key(datastore_name))
        
        ip = os.environ["REMOTE_ADDR"]

        if users.get_current_user():
            greeting.author = users.get_current_user()
        greeting.content = self.request.get('content')
        greeting.lat = data["geoplugin_latitude"]
        greeting.long = data["geoplugin_longitude"]
        greeting.put()
        query_params = {'datastore_name': datastore_name}
        self.redirect('/review?' + urllib.urlencode(query_params))

app = webapp2.WSGIApplication([ 
	('/', MainHandler),
    ('/team',TeamList),
	], debug=True)