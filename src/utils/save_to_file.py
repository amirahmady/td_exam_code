import json


def save_to_file(players, filename='players.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        for player in players:
            f.write(json.dumps(player.to_dict(), indent=4))
            f.write('\n')