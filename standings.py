import os
import requests
import json

'''
Using Sportsdata.io this is a python3 example on how to get standings. We can use this as a basic example and display the standings for conference. An API Key is required
I currently have one but omitted it here for security reasons.
'''

def get_standings():
    url = 'https://api.sportsdata.io/v3/nfl/scores/json/Standings/2020'
    r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': '%s' % 'API_KEY'})
    standings = r.json()
    print(standings)
