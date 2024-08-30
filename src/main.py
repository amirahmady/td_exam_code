
from src.helper.fetch_data import fetch_and_process_players
from src.utils.save_to_file import save_to_file


def main():
    players = fetch_and_process_players()
    save_to_file(players)

if __name__ == "__main__":
    main()