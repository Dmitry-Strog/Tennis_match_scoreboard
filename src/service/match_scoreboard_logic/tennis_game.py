from src.service.match_scoreboard_logic.player_score_tennis import PlayerScoreTennis


class TennisGame:
    def __init__(self, player1_object: PlayerScoreTennis, player2_object: PlayerScoreTennis):
        self.__player1_object = player1_object
        self.__player2_object = player2_object

    def add_point_to_player1(self):
        self.__player1_object.game_score += 1

    def add_point_to_player2(self):
        self.__player2_object.game_score += 1

    def check_game_win(self, winner_player: PlayerScoreTennis, loser_player: PlayerScoreTennis):
        if winner_player.game_score >= 4 and loser_player.game_score < 3:
            return True
        return False

    def check_deuce_win(self, winner_player: PlayerScoreTennis, loser_player: PlayerScoreTennis):
        if winner_player.game_score > 4 and (winner_player.game_score - loser_player.game_score) == 2:
            return True
        elif winner_player.game_score == 4 and loser_player.game_score == 4:
            winner_player.game_score -= 1
            loser_player.game_score -= 1

    def reset_points(self):
        self.__player1_object.game_score = 0
        self.__player2_object.game_score = 0
