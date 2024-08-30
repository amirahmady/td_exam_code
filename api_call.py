from utils.fetch_data import fetch_and_process_players


def save_to_file(players, filename='players.json'):
    with open(filename, 'w') as f:
        for player in players:
            f.write(str(player.to_dict()))
            f.write('\n')

if __name__ == "__main__":
    players = fetch_and_process_players()
    save_to_file(players)