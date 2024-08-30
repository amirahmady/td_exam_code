# Grab list of players from --> https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes?limit=5
# Save all 5 players in player object
# Update one player age to 99 and remove one player.
# Save the update list to a file

import json

import requests

url  = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes?limit=5"
response = requests.get(url)
player_data = response.json()

# print(player_data)
players = player_data['items']
# print(players)
player_list = []
# if not players:
#     return
for player in players:
    response  = requests.get(player['$ref'])
    player_list.append(response.json())

# print(player_list[0])
if player_list:
    player_list[0]['age'] = 99
    player_list.pop()

    for item in player_list:
        print(f"Name : {item['displayName']}, Age: {item['age']}")  
    

