import urllib2, json
allteams = []

http = urllib3.PoolManager()

def getTeams():
    #URL for getting all .svg grahpics                                                                                                                                                                                                                              
    data = http.request('GET', 'http://api.football-data.org/alpha/soccerseasons/354/leagueTable').data
    
    #Variables to get to where is needed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    dataDecode = json.loads(data.decode('utf8'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    teamlist = dataDecode['standing']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

    allteams = []
    #For loop to get all necessary values
    for team in teamlist:
#         class Team:
#             def __init__(self, teamname, position):
#                 self.teamname = teamname
#                 self.position = position
        t = (str(team['teamName']), team['position'])
        allteams.append(t)
    print allteams
    #Execute

getTeams()
    

    

# for t in teamlist:
#     print ('test')
#     print teamlist[t.index]['teamName']