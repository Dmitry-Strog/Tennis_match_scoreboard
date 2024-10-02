from src.service.tennis_game import TennisGame


class TennisSet:
    def __init__(self, game):
        self.player1_point: int = 0
        self.player2_point: int = 0
        self.game: TennisGame = game
        self.player1_wins: bool = False
        self.player2_wins: bool = False

    def update_point(self, player_1: int, player_2: int):
        self.game.update_point(player_1, player_2)
        if self.game.is_end_game():
            if self.game.get_winner() == "Player1":
                self.player1_point += 1
                self.game.reset_points()
                self.check_point()
            elif self.game.get_winner() == "Player2":
                self.player2_point += 1
                self.game.reset_points()
                self.check_point()


    def check_point(self):
        if self.player1_point >= 6 and 0 >= self.player2_point <= 4:
            self.player1_wins = True
        elif self.player2_point >= 5 and 0 >= self.player1_point <= 4:
            self.player2_wins = True

    def is_end_game(self):
        if self.player1_wins:
            return True
        elif self.player2_wins:
            return True

    def get_winner(self):
        if self.is_end_game():
            if self.player1_wins:
                return "Player1"
            elif self.player2_wins:
                return "Player2"

    def reset_points(self):
        self.player1_point = 0
        self.player2_point = 0
        self.player1_wins = False
        self.player2_wins = False

    def display_score_print(self):
        text = f"""
        Set:
        Player 1: {self.player1_point}
        Player 2: {self.player2_point}"""
        return print(text)
