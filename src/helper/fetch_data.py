import requests

from models.player import Player


def fetch_and_process_players():
    url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes?limit=5"
    response = requests.get(url)
    player_data = response.json()
    players = player_data['items']
    return process_players(players)

def process_players(players):
    player_list = []
    for player in players:
        response = requests.get(player['$ref'])
        player_info = response.json()
        player_obj = Player(
            id=player_info['id'],
            firstName=player_info['firstName'],
            lastName=player_info['lastName'],
            fullName=player_info['fullName'],
            displayName=player_info['displayName'],
            shortName=player_info['shortName'],
            weight=player_info['weight'],
            displayWeight=player_info['displayWeight'],
            height=player_info['height'],
            displayHeight=player_info['displayHeight'],
            age=player_info['age'],
            dateOfBirth=player_info['dateOfBirth'],
            debutYear=player_info['debutYear'],
            links=player_info['links'],
            birthPlace=player_info['birthPlace'],
            college=player_info['college'],
            slug=player_info['slug'],
            headshot=player_info['headshot'],
            jersey=player_info['jersey'],
            position=player_info['position'],
            injuries=player_info['injuries'],
            linked=player_info['linked'],
            team=player_info['team'],
            teams=player_info['teams'],
            statistics=player_info['statistics'],
            notes=player_info['notes'],
            contracts=player_info['contracts'],
            experience=player_info['experience'],
            collegeAthlete=player_info['collegeAthlete'],
            active=player_info['active'],
            eventLog=player_info['eventLog'],
            draft=player_info['draft'],
            status=player_info['status']
        )
        player_list.append(player_obj)
    return player_list