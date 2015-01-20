import urllib3, json
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
    for idx, t in enumerate(teamlist):
        teamlink = teamlist[int(idx)]['_links']['team']['href']
        name = t['teamName']
        position = t['position']

        print teamlink + '  ' + name
        
        
        
    
getTeams()
    

# for t in teamlist:
#     print ('test')
#     print teamlist[t.index]['teamName']
    
#Would using class objects be of any use?
#maybe will look into it, just want to get all the values I need first
#
                 