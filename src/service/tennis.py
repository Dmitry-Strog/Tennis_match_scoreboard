from src.service.tennis_game import TennisGame
from src.service.tennis_match import TennisMatch
from src.service.tennis_set import TennisSet


class Tennis:
    def __init__(self):
        self.game = TennisGame()
        self.tennis_set = TennisSet(self.game)
        self.match = TennisMatch(self.tennis_set)

    def tennis_game(self):
        return self.game.display_score_print()

    def tennis_sett(self):
        return self.tennis_set.display_score_print()

    def tennis_match(self):
        return self.match.display_score_print()


tennis = Tennis()
for _ in range():
    tennis.match.update_point(0, 1)
    tennis.match.update_point(1, 0)
tennis.tennis_game()
tennis.tennis_sett()
tennis.tennis_match()