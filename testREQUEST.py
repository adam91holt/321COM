import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'http://api.football-data.org/alpha/soccerseasons/354/leagueTable')

print r.data