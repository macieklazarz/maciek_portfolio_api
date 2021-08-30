from django.http import HttpResponse
from django.shortcuts import render
import http.client
import json

def homepage(request):
    return render(request, 'index.html')

def football_api(request):
    if request.POST:
    	connection = http.client.HTTPConnection('api.football-data.org')
    	headers={'X-Auth-Token':'c563e3df9d5f4541b126072eb0f0eff1'}
    	val = request.POST["league"]
    	liga ="dupa"
    	if val == 'Bundesliga':
    		connection.request('GET', '/v2/competitions/BL1/standings', None, headers )
    	elif val == 'Premier League':
    		connection.request('GET', '/v2/competitions/PL/standings', None, headers )
    	elif val == 'Ederdivise':
    		connection.request('GET', '/v2/competitions/DED/standings', None, headers )
    	elif val == 'Primiera Division':
    		connection.request('GET', '/v2/competitions/PD/standings', None, headers )
    	elif val == 'Ligue 1':
    		connection.request('GET', '/v2/competitions/FL1/standings', None, headers )
    	elif val == 'Serie A':
    		connection.request('GET', '/v2/competitions/SA/standings', None, headers )
    	dane1 = json.loads(connection.getresponse().read().decode())
    	dane2 = dane1.get("standings")
    	dane3 = dane2[0]
    	dane4 = dane3['table']
    	# rows = [['team_name','games', 'won', 'draw', 'lost', 'goals scored', 'goal lost', 'points']]
    	rows = []
    	for dane in dane4:
    		team = dane.get("team")
    		team2 = team.get("name")
    		rows.append([team2, dane['playedGames'], dane['won'], dane['lost'], dane['draw'], dane['goalsFor'], dane['goalsAgainst'], dane['points']])
    	print(f"val={val}")
    	return render(request, 'football_api.html',{"tabela": rows, "liga":val})
    return render(request, 'football_api.html')

def xlsxtocsv(request):
    return render(request, 'xlsxtocsv.html')


	