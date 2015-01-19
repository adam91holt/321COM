	 from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2
import jinja2
import urllib
import os
from datetime import datetime
import urllib2
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')),
    extensions=['jinja2.ext.autoescape'])
	 
class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello World!')
        
        
class teams(ndb.Model):
    """Modeling the data store for teams"""
    teamname = ndb.StringProperty(indexed=False)
    initials = ndb.StringProperty()
    twitterurl = ndb.StringProperty()
    stadiumlong = ndb.StringProperty()
    stadiumlat = ndb.StringProperty()
    youtubeurl = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

def team_key(datastore_name ='teams'):   
    """Constructs a Datastore key for a Guestbook entity with datastore_name."""
    return ndb.Key('teams', datastore_name)
    
""" setting up the data store for fetching the lists of teams"""
class TeamList(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url(self.request.path)
	datastore_name = self.request.get('teams', 'teams')
        teams_query = team.query(
            ancestor=guestbook_key(datastore_name)).order(-teams.teamname)
        teams = teams_query.fetch(10)
        if user:
        	template = JINJA_ENVIRONMENT.get_template('teams.html')
        	template_values = {
		    'teams': teams,
		    'datastore_name': urllib.quote_plus(datastore_name),
            'user': user.nickname(),
            'url_logout': logout_url,
            'url_logout_text': 'Log out',
                
        	}
        	self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        datastore_name = self.request.get('datastore_name',
                                          'teams')
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
	('/', MainHandler)
	], debug=True)