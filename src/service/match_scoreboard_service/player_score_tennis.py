class PlayerScoreTennis:
    SCORE_MAPPING_GAME = {
        0: 0, "15": 1, "30": 2, "40": 3, "AD": 4
    }

    def __init__(self, name, score=None):
        if score is not None:
            number_game_score = self.SCORE_MAPPING_GAME[score[name]["game_score"]]
            self.name = name
            self.game_score = int(number_game_score)
            self.tie_break_score = score[name]["tie_break_score"]
            self.set_score = score[name]["set_score"]
            self.match_score = score[name]["match_score"]
        else:
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
