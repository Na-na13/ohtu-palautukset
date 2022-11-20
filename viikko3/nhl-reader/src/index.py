from datetime import datetime
from player_reader import PlayerReader
from player_stats import PlayerStats

def sum_of_goals_and_assists(player):
    return int(player.goals)+int(player.assists)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print(f"Players from FIN {datetime.now()}")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
