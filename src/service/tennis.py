from src.service.tennis_game import TennisGame
from src.service.tennis_match import TennisMatch
from src.service.tennis_set import TennisSet
from src.service.tennis_tie_break import TieBreak


class Tennis:
    def __init__(self):
        self.game = TennisGame()
        self.tie_break = TieBreak()
        self.tennis_set = TennisSet(self.game, self.tie_break)
        self.match = TennisMatch(self.tennis_set)

    def tennis_game(self):
        if self.tennis_set.tie_break_flag:
            return self.tie_break.display_score_print()
        return self.game.display_score_print()

    def tennis_sett(self):
        return self.tennis_set.display_score_print()

    def tennis_match(self):
        return self.match.display_score_print()


tennis = Tennis()
for _ in range(4):
    tennis.match.update_point(1, 0)

tennis.tennis_game()
tennis.tennis_sett()
tennis.tennis_match()
