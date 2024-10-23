from src.service.match_scoreboard_logic.player_score_tennis import PlayerScoreTennis


class TennisMatch:
    def __init__(self, player1_object: PlayerScoreTennis, player2_object: PlayerScoreTennis):
        self.__player1_object = player1_object
        self.__player2_object = player2_object

    def add_point_to_player1(self):
        self.__player1_object.match_score += 1

    def add_point_to_player2(self):
        self.__player2_object.match_score += 1

    def check_match_win(self, winner_player: PlayerScoreTennis, loser_player: PlayerScoreTennis):
        if winner_player.match_score >= 2 and (winner_player.match_score - loser_player.match_score) == 2:
            return True
        elif winner_player.match_score >= 3 and loser_player.match_score < 3:
            return True

    def get_winner(self, winner_player: PlayerScoreTennis, loser_player: PlayerScoreTennis):
        if self.check_match_win(winner_player, loser_player):
            return winner_player
