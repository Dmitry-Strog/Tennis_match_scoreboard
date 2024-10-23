class PlayerScoreTennis:

    SCORE_MAPPING_GAME = {
        0: 0, "15": 1, "30": 2, "40": 3, "AD": 4
    }

    def __init__(self, name, score=None):
        self.name = name
        if score is not None:
            self.game_score = self.convert_game_score(score[name]["game_score"])
            self.tie_break_score = score[name]["tie_break_score"]
            self.set_score = score[name]["set_score"]
            self.match_score = score[name]["match_score"]
        else:
            self.game_score = 0
            self.tie_break_score = 0
            self.set_score = 0
            self.match_score = 0

    def convert_game_score(self, game_score):
        return self.SCORE_MAPPING_GAME[game_score]

    def to_dict(self):
        return {
            "game_score": self.game_score,
            "tie_break_score": self.tie_break_score,
            "set_score": self.set_score,
            "match_score": self.match_score,
        }
