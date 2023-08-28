class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, player_name):
        return self.players.append(player_name)
    
    def has_player(self, player_name):
        for player in self.players:
            if player == player_name:
                return True
        return False
    
    def play_game(self, did_win):
        if did_win:
            self.points += 3
            return self.points