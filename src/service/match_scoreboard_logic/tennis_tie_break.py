from src.service.match_scoreboard_logic.player_score_tennis import PlayerScoreTennis


class TieBreak:
    TIEBREAK_WIN_THRESHOLD = 7

    def __init__(self, player1_object: PlayerScoreTennis, player2_object: PlayerScoreTennis):
        self.__player1_object = player1_object
        self.__player2_object = player2_object

    def add_point_to_player1(self):
        self.__player1_object.tie_break_score += 1

    def add_point_to_player2(self):
        self.__player2_object.tie_break_score += 1

    def check_tie_break_win(self, winner_player: PlayerScoreTennis, loser_player: PlayerScoreTennis):
        if (winner_player.tie_break_score >= self.TIEBREAK_WIN_THRESHOLD
                and (winner_player.tie_break_score - loser_player.tie_break_score) == 2):
            return True
        elif winner_player.tie_break_score >= self.TIEBREAK_WIN_THRESHOLD and loser_player.tie_break_score < 6:
            return True

    def reset_points(self):
        self.__player1_object.tie_break_score = 0
        self.__player2_object.tie_break_score = 0
