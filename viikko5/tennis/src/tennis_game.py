class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = {player1_name: 0, player2_name: 0}
        self.scores = ["Love","Fifteen","Thirty","Forty"]

    def won_point(self, player_name):
        self.players[player_name] += 1

    def get_score(self):
        players = list(self.players.keys())
        if self.players[players[0]] == self.players[players[1]]:
            return self.tie_set(players[0])

        elif self.players[players[0]] >= 4 or self.players[players[1]] >= 4:
            minus_result = self.players[players[0]] - self.players[players[1]]

            if minus_result == 1:
                return "Advantage player1"
            elif minus_result == -1:
                return "Advantage player2"
            elif minus_result >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
 
        else:
            return f"{self.scores[self.players[players[0]]]}-{self.scores[self.players[players[1]]]}"

    def tie_set(self, key):
        if self.players[key] < 4:
            return f"{self.scores[self.players[key]]}-All" 
        return f"Deuce"