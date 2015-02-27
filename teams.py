import urllib2, json

API_TOKEN = 'c352b328988b454483566956e6882442'

def allTeams():
    #Actual API request
    req = urllib2.Request('http://api.football-data.org/alpha/soccerseasons/354/leagueTable')
    req.add_header('X-Auth-Token', API_TOKEN)
    resp = urllib2.urlopen(req)
    content = resp.read()
    #Decode to JSON                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    dataDecode = json.loads(content.decode('utf8'))    
    #Store all teams
    teams = dataDecode['standing']
    return teams



def tableStandings():
    #URL for getting all teams     
    #Actual API request
    req = urllib2.Request('http://api.football-data.org/alpha/soccerseasons/354/leagueTable')
    req.add_header('X-Auth-Token', API_TOKEN)
    resp = urllib2.urlopen(req)
    content = resp.read()
    #Decode to JSON                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    dataDecode = json.loads(content.decode('utf8'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    teamlist = dataDecode['standing']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    #Stores all teams and positions
    allteams = []
    #For loop to get all necessary values
    for team in teamlist:
        t = (str(team['teamName']), team['position'])
        allteams.append(t)
        #End Loop
    return allteams
    

#arg gets passed through via the url in the main file
def teamList(arg):
    #Array to store all players in... will be store in tuples
    teamPlayers = []
    #All teams
    teams = allTeams()
    #For loops to search all teams with arguement and then get players into the teamPlayers array
    for t in teams:
        #Get each club name
        club = t['teamName']
        #Finds the team from the one that was passed throuh
        if arg in club:
            #Get the url for the club
            cluburl = t['_links']['team']['href']
            #Open up the url
            req = urllib2.Request(cluburl)
            req.add_header('X-Auth-Token', API_TOKEN)
            resp = urllib2.urlopen(req)
            content = resp.read()
            #Convert JSON
            clubJSON = json.loads(content.decode('utf8')) 
            #Players URL
            playersurl = clubJSON['_links']['players']['href']
            #Get all players
            openplayers = urllib2.urlopen(playersurl).read()
            #Convert JSON
            players = json.loads(openplayers.decode('utf8'))
            #Variable for all the players
            player = players['players']
            #For loop to put in every team player
            for p in player:
                person = (p['jerseyNumber'], p['name'], p['position'])
                teamPlayers.append(person)
                print person
    return teamPlayers
