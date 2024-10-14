class PlayerScoreTennis:
    def __init__(self, name):

        self.name = name
        self.game_score = 0
        self.tie_break_score = 0
        self.set_score = 0
        self.match_score = 0

    def to_dict(self):
        return {
            "game_score": self.game_score,
            "tie_break_score": self.tie_break_score,
            "set_score": self.set_score,
            "match_score": self.match_score,
        }
