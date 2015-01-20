import urllib2, json

data = urllib2.urlopen('http://api.football-data.org/alpha/soccerseasons/354/leagueTable').read()
#Variables to get to where is needed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
dataDecode = json.loads(data.decode('utf8'))    
#Store all teams
teamlist = dataDecode['standing']

arg = 'Chelsea'

teamPlayers = []

for t in teamlist:
    #Get each club name
    club = t['teamName']
    
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
        player = players['players']
        for p in player:
            person = (p['jerseryNumber'], p['name'], p['position'])
            teamPlayers.append(person)
        print teamPlayers

        
        




# Grab all teams

# Take an arguement from the url

# Search array for that arguement and find out where it is

# do more querys on api