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

    def update_point(self, player_1: int, player_2: int): # Переделать тестевый вариант
        obj = self.game
        if self.tie_break_flag:
            obj = self.tie_break
            obj.update_point(player_1, player_2)
            if obj.is_end_game():
                if obj.get_winner() == "Player1":
                    self.player1_wins = True
                elif obj.get_winner() == "Player2":
                    self.player2_wins = True
        else:
            obj.update_point(player_1, player_2)
            if obj.is_end_game():
                if obj.get_winner() == "Player1":
                    self.player1_point += 1
                    self.check_point()
                elif obj.get_winner() == "Player2":
                    self.player2_point += 1
                    self.check_point()
                obj.reset_points()


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
