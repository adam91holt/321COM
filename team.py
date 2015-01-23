import urllib2, json

#Actual API request
data = urllib2.urlopen('http://api.football-data.org/alpha/soccerseasons/354/leagueTable').read()
#Decode to JSON                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
dataDecode = json.loads(data.decode('utf8'))    
#Store all teams
teamlist = dataDecode['standing']

#Argument - this will later be passed in via URL
arg = 'Manchester City'

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

for p in teamPlayers:
    print 'Number: ', p[0], ' Name: ', p[1], ' Position: ', p[2] 

# Grab all teams

# Take an arguement from the url

# Search array for that arguement and find out where it is

# do more querys on api