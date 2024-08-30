"""
This module fetches a list of NFL players, updates one player's age, removes one player,
and saves the updated list to a file.
"""

import json

import requests


def fetch_players(url):
    """Fetch the list of players from the given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()['items']
    except requests.RequestException as e:
        print(f"Error fetching players: {e}")
        return []

def fetch_player_details(player_url):
    """Fetch player details from the given URL."""
    try:
        response = requests.get(player_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching player details: {e}")
        return None

def update_and_save_players(player_list, filename='updated_players.json'):
    """Update one player's age, remove one player, and save the list to a file."""
    if player_list:
        player_list[0]['age'] = 99
        player_list.pop()

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(player_list, f, indent=4)

        for item in player_list:
            print(f"Name: {item['displayName']}, Age: {item['age']}")

def main():
    """Main function to fetch, update, and save player data."""
    url = ("https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/"
           "2023/teams/18/athletes?limit=5")
    players = fetch_players(url)
    player_list = []

    for player in players:
        player_details = fetch_player_details(player['$ref'])
        if player_details:
            player_list.append(player_details)

    update_and_save_players(player_list)

if __name__ == "__main__":
    main()
