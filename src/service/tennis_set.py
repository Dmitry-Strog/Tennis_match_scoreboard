from src.service.tennis_game import TennisGame
from src.service.tennis_tie_break import TieBreak


class TennisSet:
    def __init__(self, game, tie_break):
        self.player1_point: int = 0
        self.player2_point: int = 0
        self.game: TennisGame = game
        self.tie_break: TieBreak = tie_break
        self.tie_break_flag: bool = False
        self.player1_wins: bool = False
        self.player2_wins: bool = False

    def update_point(self, player_1: int, player_2: int):
        if self.tie_break_flag:
            self.update_tie_break_point(player_1, player_2)
        else:
            self.update_game_point(player_1, player_2)

    def update_game_point(self, player_1: int, player_2: int):
        self.game.update_point(player_1, player_2)
        if self.game.is_end_game():
            self.add_game_point(self.game.get_winner())
            self.game.reset_points()

    def update_tie_break_point(self, player_1: int, player_2: int):
        self.tie_break.update_point(player_1, player_2)
        if self.tie_break.is_end_game():
            self.set_tie_break_winner(self.tie_break.get_winner())
            self.tie_break.reset_points()

    def add_game_point(self, winner: str):
        if winner == "Player1":
            self.player1_point += 1
        elif winner == "Player2":
            self.player2_point += 1
        self.check_point()

    def set_tie_break_winner(self, winner: str):
        if winner == "Player1":
            self.player1_wins = True
        elif winner == "Player2":
            self.player2_wins = True

    def check_point(self):
        if self.player1_point >= 6 and (self.player1_point - self.player2_point) == 2:
            self.player1_wins = True
        elif self.player2_point >= 6 and (self.player2_point - self.player1_point) == 2:
            self.player2_wins = True
        elif self.player1_point >= 6 and self.player2_point < 5:
            self.player1_wins = True
        elif self.player2_point >= 6 and self.player1_point < 5:
            self.player2_wins = True
        elif self.player1_point == 6 and self.player2_point == 6:
            self.tie_break_flag = True

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
        self.tie_break_flag: bool = False

    def display_score_print(self):
        text = f"""
        Set:
        Player 1: {self.player1_point}
        Player 2: {self.player2_point}"""
        return print(text)
