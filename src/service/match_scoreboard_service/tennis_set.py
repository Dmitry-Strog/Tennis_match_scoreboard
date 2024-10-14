from src.service.match_scoreboard_service.player_score_tennis import PlayerScoreTennis


class TennisSet:

    def __init__(self, player1_object: PlayerScoreTennis, player2_object: PlayerScoreTennis):
        self.player1_object = player1_object
        self.player2_object = player2_object

    def add_point_to_player1(self):
        self.player1_object.set_score += 1

    def add_point_to_player2(self):
        self.player2_object.set_score += 1

    def check_set_win(self, winner_player: PlayerScoreTennis, loser_player: PlayerScoreTennis):

        if winner_player.set_score >= 6 and (winner_player.set_score - loser_player.set_score) == 2:
            return True
        elif winner_player.set_score >= 6 and loser_player.set_score < 5:
            return True

    def is_tie_break(self, winner_player: PlayerScoreTennis, loser_player: PlayerScoreTennis):
        if winner_player.set_score == 6 and loser_player.set_score == 6:
            return True

    def reset_points(self):
        self.player1_object.set_score = 0
        self.player2_object.set_score = 0

