import os
import requests
import json

'''
Using Sportsdata.io this is a python3 example on how to get standings. We can use this as a basic example and display the standings for conference. An API Key is required
I currently have one but omitted it here for security reasons.
'''

import os
import requests
import json

API_KEY = 'API_KEY'
SUB_KEY = 'Ocp-Apim-Subscription-Key'

def get_are_games_in_progress():
    url = 'https://api.sportsdata.io/v3/nfl/scores/json/AreAnyGamesInProgress'
    r = requests.get(url, headers={'SUB_KEY': '%s' % 'API_KEY'})
    games_in_progress = r.json()
    print(games_in_progress)

def get_data_formatted_key_value(url, sub_key, api_key):
    url = url
    r = requests.get(url, headers={sub_key: '%s' % api_key})
    output = r.json()
    for x in range(len(output)):
        for key, value in output[x].items():
            print(key, ":", value)

def get_player_details(url, sub_key, api_key): #Need to feed ID into URL
    url = url
    r = requests.get(url, headers={sub_key: '%s' % api_key})
    output = r.json()
    print(output)

#get_are_games_in_progress()
#get_data_formatted_key_value('https://api.sportsdata.io/v3/nfl/scores/json/Standings/2020', SUB_KEY, API_KEY)
#get_data_formatted_key_value('https://api.sportsdata.io/v3/nfl/scores/json/Byes/2020', SUB_KEY, API_KEY)
#get_data_formatted_key_value('https://api.sportsdata.io/v3/nfl/scores/json/Players', SUB_KEY, API_KEY)
#get_data_formatted_key_value('https://api.sportsdata.io/v3/nfl/scores/json/FreeAgents', SUB_KEY, API_KEY)
#get_player_details('https://api.sportsdata.io/v3/nfl/scores/json/Player/732', SUB_KEY, API_KEY) MATT RYAN
#get_data_formatted_key_value('https://api.sportsdata.io/v3/nfl/scores/json/Rookies/2020', SUB_KEY, API_KEY)
#get_data_formatted_key_value('https://api.sportsdata.io/v3/nfl/scores/json/Players/SEA', SUB_KEY, API_KEY) Need Team ID i.e SEA
#get_data_formatted_key_value('https://api.sportsdata.io/v3/nfl/stats/json/ProBowlers/2019', SUB_KEY, API_KEY)
