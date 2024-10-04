from src.service.tennis_game import TennisGame


class TieBreak(TennisGame):
    def __init__(self):
        super().__init__()
        self.player1_point: int = 0
        self.player2_point: int = 0
        self.player1_wins: bool = False
        self.player2_wins: bool = False

    def update_point(self, player_1: int, player_2: int):
        if player_1:
            self.player1_point += 1
        elif player_2:
            self.player2_point += 1
        self.check_point()

    def check_point(self):
        if self.player1_point >= 7 and (self.player1_point - self.player2_point) == 2:
            self.player1_wins = True
        elif self.player2_point >= 7 and (self.player2_point - self.player1_point) == 2:
            self.player2_wins = True
        elif self.player1_point >= 7 and self.player2_point < 6:
            self.player1_wins = True
        elif self.player2_point >= 7 and self.player1_point < 6:
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

    def display_score_print(self):
        text = f"""
        TieBreak:
        Player 1: {self.player1_point}
        Player 2: {self.player2_point}"""
        return print(text)

    def reset_points(self):
        self.player1_point = 0
        self.player2_point = 0
        self.player1_wins = False
        self.player2_wins = False
