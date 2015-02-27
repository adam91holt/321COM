from google.appengine.ext import db

#This basically is the model of the data that is entered into the datastore
class Team(db.Model):
    teamName = db.StringProperty()
    twitter = db.StringProperty()
    youtube = db.StringProperty()
    lon = db.FloatProperty()
    lat = db.FloatProperty()
    stadium = db.StringProperty()
    emblem = db.StringProperty()
    wikipedia = db.StringProperty()

def dataStoreTeams():
    #Add all 20 teams but not wolverhampton like reiss did
    Team(key_name='Chelsea', teamName='Chelsea', twitter='@chelseafc', youtube='chelseafc', lon= -0.192541, lat= 51.482505, stadium='Stamford Bridge', emblem = 'http://upload.wikimedia.org/wikipedia/de/5/5c/Chelsea_crest.svg', wikipedia = '7473').put()
    Team(key_name='ManCity', teamName='Manchester City', twitter='@MCFC', youtube='mcfcofficial', lon= -2.200459, lat=53.483087, stadium='Etihad Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/f/fd/ManCity.svg', wikipedia = '165813').put()
    Team(key_name='Southampton', teamName='Southampton', twitter='@SouthamptonFC', youtube='theofficialsaints', lon= -1.390984, lat=50.906178, stadium='St Mary\'s Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/c/c9/FC_Southampton.svg', wikipedia = '81576').put()
    Team(key_name='ManU', teamName='Manchester United', twitter='@ManUtd', youtube='FullTimeDevils', lon= -2.291297, lat=53.463021, stadium='Old Trafford', emblem = 'http://upload.wikimedia.org/wikipedia/de/d/da/Manchester_United_FC.svg', wikipedia = '19961').put()
    Team(key_name='Arsenal', teamName='Arsenal', twitter='@arsenal', youtube='ArsenalTour', lon= 0.108558899999934510, lat=51.554947700000010000, stadium='The Emirates', emblem = 'http://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg', wikipedia = '2174').put()
    Team(key_name='Tottenham', teamName='Tottenham Hotspur', twitter='@SpursOfficial', youtube='spursofficial', lon= -0.066430, lat=51.603278, stadium='White Hart Lane', emblem = 'http://upload.wikimedia.org/wikipedia/de/b/b4/Tottenham_Hotspur.svg', wikipedia = '68198').put()
    Team(key_name='West Ham', teamName='West Ham United', twitter='@whufc_official', youtube='UCCNOsmurvpEit9paBOzWtUg', lon=0.039273, lat=51.532024, stadium='Boleyn Ground', emblem = 'http://upload.wikimedia.org/wikipedia/de/e/e0/West_Ham_United_FC.svg', wikipedia = '46417').put()
    Team(key_name='Liverpool', teamName='Liverpool', twitter='@LFC', youtube='LiverpoolFC', lon= -2.960873, lat=53.430995, stadium='Anfield', emblem = 'http://upload.wikimedia.org/wikipedia/de/0/0a/FC_Liverpool.svg', wikipedia = '18119').put()
    Team(key_name='Swansea', teamName='Swansea City', twitter='@SwansOfficial', youtube='SWANSPLAYER', lon= -3.935264, lat=51.642737, stadium='Liberty Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/a/ab/Swansea_City_Logo.svg', wikipedia = '451169').put()
    Team(key_name='Stoke', teamName='Stoke City', twitter='@stokecity', youtube='UCmFPjHUFr0hyE6eFGvCm7IA', lon= -2.175507, lat=52.988329, stadium='Britannia Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/a/a3/Stoke_City.svg', wikipedia = '203434').put()
    Team(key_name='Newcastle', teamName='Newcastle United', twitter='@NUFC', youtube='NUFCOfficial1892', lon= -1.621667, lat=54.975593, stadium='St James\' Park', emblem = 'http://upload.wikimedia.org/wikipedia/de/5/56/Newcastle_United_Logo.svg', wikipedia = '57802').put()
    Team(key_name='Everton', teamName='Everton', twitter='@Everton', youtube='OfficialEverton', lon= -2.966448, lat=53.438979, stadium='Goodison Park', emblem = 'http://upload.wikimedia.org/wikipedia/de/f/f9/Everton_FC.svg', wikipedia = '91155').put()
    Team(key_name='Crystal', teamName='Crystal Palace', twitter='@CPFC', youtube='OfficialCPFC', lon= -0.085657, lat=51.398347, stadium='Selhurst Park', emblem = 'http://upload.wikimedia.org/wikipedia/de/b/bf/Crystal_Palace_F.C._logo_(2013).png', wikipedia = '385313').put()
    Team(key_name='West Bromwich', teamName='West Bromwich Albion', twitter='@WBAFCofficial', youtube='OfficialAlbion', lon= -1.964002, lat=52.509599, stadium='The Hawthorns', emblem = 'http://upload.wikimedia.org/wikipedia/de/8/8b/West_Bromwich_Albion.svg', wikipedia = '33921').put()
    Team(key_name='Sunderland', teamName='Sunderland', twitter='@SunderlandAFC', youtube='sunderlandafc', lon= -1.388500, lat=54.914623, stadium='Stadium of Light', emblem = 'http://upload.wikimedia.org/wikipedia/de/6/60/AFC_Sunderland.svg', wikipedia = '184474').put()
    Team(key_name='Villa', teamName='Aston Villa', twitter='@avfcofficial', youtube='avfcofficial', lon= -1.8862340000000586, lat=52.510129, stadium='Villa Park', emblem = 'http://upload.wikimedia.org/wikipedia/de/9/9f/Aston_Villa_logo.svg', wikipedia = '42173').put()
    Team(key_name='Burnley', teamName='Burnley', twitter='@BurnleyOfficial', youtube='officialburnleyfc', lon= -2.230209, lat=53.788947, stadium='Turf Moor', emblem = 'http://upload.wikimedia.org/wikipedia/de/8/87/Burnley_FC.gif', wikipedia = '376725').put()
    Team(key_name='Hull', teamName='Hull City', twitter='@HullFCNews', youtube='HCAFCOfficial', lon= -0.367735, lat=53.746560, stadium='KC Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/de/a/a9/Hull_City_AFC.svg', wikipedia = '1095938').put()
    Team(key_name='QPR', teamName='Queens Park Rangers', twitter='@QPRFC', youtube='OfficialQPR', lon= -0.232914, lat=51.509689, stadium='Loftus Road', emblem = 'http://upload.wikimedia.org/wikipedia/de/d/d4/Queens_Park_Rangers.svg', wikipedia = '84588').put()
    Team(key_name='Leicester', teamName='Leicester City', twitter='@OfficialFOXES', youtube='LCFCOfficial', lon= -1.141543, lat=52.620109, stadium='King Power Stadium', emblem = 'http://upload.wikimedia.org/wikipedia/en/6/63/Leicester02.png', wikipedia = '298602').put()
