from typing import Tuple

from src.service.match_scoreboard_logic.player_score_tennis import PlayerScoreTennis
from src.service.match_scoreboard_logic.tennis_game import TennisGame
from src.service.match_scoreboard_logic.tennis_match import TennisMatch
from src.service.match_scoreboard_logic.tennis_set import TennisSet
from src.service.match_scoreboard_logic.tennis_tie_break import TieBreak


class ScoreboardTennis:

    SCORE_MAPPING_GAME = {
        0: 0, 1: "15", 2: "30", 3: "40", 4: "AD"
    }

    def __init__(self, player_name1, player_name2, score=None):
        self.player1 = PlayerScoreTennis(player_name1, score)
        self.player2 = PlayerScoreTennis(player_name2, score)
        self.game = TennisGame(self.player1, self.player2)
        self.set = TennisSet(self.player1, self.player2)
        self.tie_break = TieBreak(self.player1, self.player2)
        self.match = TennisMatch(self.player1, self.player2)

        self.winner_player = None

    def simulation_scoreboard(self, point_winner):
        winner_player, loser_player = self.get_players(point_winner)
        if self.set.is_tie_break(self.player1, self.player2):
            self.update_tie_break(winner_player, loser_player)
        else:
            self.update_game(winner_player, loser_player)
        if self.winner_player is not None:
            return self.winner_player

    def get_players(self, point_player) -> Tuple[PlayerScoreTennis, PlayerScoreTennis]:
        if point_player == 1:
            return self.player1, self.player2
        elif point_player == 2:
            return self.player2, self.player1

    def update_game(self, winner_player, loser_player):

        if winner_player is self.player1:
            self.game.add_point_to_player1()
        elif winner_player is self.player2:
            self.game.add_point_to_player2()

        if self.game.check_game_win(winner_player, loser_player):
            self.update_set(winner_player, loser_player)
            self.game.reset_points()

        if self.game.check_deuce_win(winner_player, loser_player):
            self.update_set(winner_player, loser_player)
            self.game.reset_points()

    def update_set(self, winner_player, loser_player):

        if winner_player is self.player1:
            self.set.add_point_to_player1()
        elif winner_player is self.player2:
            self.set.add_point_to_player2()

        if self.set.is_tie_break(winner_player, loser_player):
            return

        elif self.set.check_set_win(winner_player, loser_player):
            self.update_match(winner_player, loser_player)
            self.set.reset_points()

    def update_tie_break(self, winner_player, loser_player):

        if winner_player is self.player1:
            self.tie_break.add_point_to_player1()
        elif winner_player is self.player2:
            self.tie_break.add_point_to_player2()

        if self.tie_break.check_tie_break_win(winner_player, loser_player):
            self.update_match(winner_player, loser_player)
            self.set.reset_points()
            self.tie_break.reset_points()

    def update_match(self, winner_player, loser_player):

        if winner_player is self.player1:
            self.match.add_point_to_player1()
        elif winner_player is self.player2:
            self.match.add_point_to_player2()
        if self.match.check_match_win(winner_player, loser_player):
            self.winner_player = self.match.get_winner(winner_player, loser_player)

    def to_dict(self):
        player1_dict = self.player1.to_dict()
        player2_dict = self.player2.to_dict()
        player1_dict["game_score"] = self.SCORE_MAPPING_GAME[int(self.player1.game_score)]
        player2_dict["game_score"] = self.SCORE_MAPPING_GAME[int(self.player2.game_score)]

        return {
            self.player1.name: player1_dict,
            self.player2.name: player2_dict,
        }
