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
        self.__player1 = PlayerScoreTennis(player_name1, score)
        self.__player2 = PlayerScoreTennis(player_name2, score)
        self.__game = TennisGame(self.__player1, self.__player2)
        self.__set = TennisSet(self.__player1, self.__player2)
        self.__tie_break = TieBreak(self.__player1, self.__player2)
        self.__match = TennisMatch(self.__player1, self.__player2)

        self.__winner_player = None

    @property
    def winner_player(self):
        return self.__winner_player

    def simulation_scoreboard(self, point_winner):
        winner_player, loser_player = self.__get_players(point_winner)
        if self.__set.is_tie_break(self.__player1, self.__player2):
            self.__update_tie_break(winner_player, loser_player)
        else:
            self.__update_game(winner_player, loser_player)

    def __get_players(self, point_player) -> Tuple[PlayerScoreTennis, PlayerScoreTennis]:
        if point_player == 1:
            return self.__player1, self.__player2
        elif point_player == 2:
            return self.__player2, self.__player1

    def __update_game(self, winner_player, loser_player):

        if winner_player is self.__player1:
            self.__game.add_point_to_player1()
        elif winner_player is self.__player2:
            self.__game.add_point_to_player2()

        if self.__game.check_game_win(winner_player, loser_player):
            self.__update_set(winner_player, loser_player)
            self.__game.reset_points()

        if self.__game.check_deuce_win(winner_player, loser_player):
            self.__update_set(winner_player, loser_player)
            self.__game.reset_points()

    def __update_set(self, winner_player, loser_player):

        if winner_player is self.__player1:
            self.__set.add_point_to_player1()
        elif winner_player is self.__player2:
            self.__set.add_point_to_player2()

        if self.__set.is_tie_break(winner_player, loser_player):
            return

        elif self.__set.check_set_win(winner_player, loser_player):
            self.__update_match(winner_player, loser_player)
            self.__set.reset_points()

    def __update_tie_break(self, winner_player, loser_player):

        if winner_player is self.__player1:
            self.__tie_break.add_point_to_player1()
        elif winner_player is self.__player2:
            self.__tie_break.add_point_to_player2()

        if self.__tie_break.check_tie_break_win(winner_player, loser_player):
            self.__update_match(winner_player, loser_player)
            self.__set.reset_points()
            self.__tie_break.reset_points()

    def __update_match(self, winner_player, loser_player):
        if winner_player is self.__player1:
            self.__match.add_point_to_player1()
        elif winner_player is self.__player2:
            self.__match.add_point_to_player2()
        if self.__match.check_match_win(winner_player, loser_player):
            self.__winner_player = self.__match.get_winner(winner_player, loser_player)

    def to_dict(self):
        player1_dict = self.__player1.to_dict()
        player2_dict = self.__player2.to_dict()
        player1_dict["game_score"] = self.SCORE_MAPPING_GAME[int(self.__player1.game_score)]
        player2_dict["game_score"] = self.SCORE_MAPPING_GAME[int(self.__player2.game_score)]

        return {
            self.__player1.name: player1_dict,
            self.__player2.name: player2_dict,
        }


match = ScoreboardTennis("test1", "test2")

for _ in range(20):
    match.simulation_scoreboard(1)
    match.simulation_scoreboard(1)
    match.simulation_scoreboard(2)
    match.simulation_scoreboard(2)

match.simulation_scoreboard(1)
match.simulation_scoreboard(1)
print(match.to_dict())
