from src.service.match_scoreboard_service.player_score_tennis import PlayerScoreTennis


class TieBreak:
    def __init__(self, player1_object: PlayerScoreTennis, player2_object: PlayerScoreTennis):
        self.player1_object = player1_object
        self.player2_object = player2_object

    def add_point_to_player1(self):
        self.player1_object.tie_break_score += 1

    def add_point_to_player2(self):
        self.player2_object.tie_break_score += 1

    def check_tie_break_win(self, winner_player: PlayerScoreTennis, loser_player: PlayerScoreTennis):
        if winner_player.tie_break_score >= 7 and (winner_player.tie_break_score - loser_player.tie_break_score) == 2:
            return True
        elif winner_player.tie_break_score >= 7 and loser_player.tie_break_score < 6:
            return True

    def reset_points(self):
        self.player1_object.tie_break_score = 0
        self.player2_object.tie_break_score = 0