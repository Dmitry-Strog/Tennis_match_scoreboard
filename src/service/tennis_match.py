from src.service.tennis_set import TennisSet


class TennisMatch:
    def __init__(self, tennis_set):
        self.player1_point: int = 0
        self.player2_point: int = 0
        self.tennis_set: TennisSet = tennis_set

    def update_point(self, player_1: int, player_2: int):
        self.tennis_set.update_point(player_1, player_2)
        if self.tennis_set.is_end_game():
            if self.tennis_set.get_winner() == "Player1":
                self.player1_point += 1
                self.tennis_set.reset_points()
                self.check_point()
            elif self.tennis_set.get_winner() == "Player2":
                self.player2_point += 1
                self.tennis_set.reset_points()
                self.check_point()

    def check_point(self):
        if self.player1_point >= 3 and self.player2_point < 3:
            return print("Winner player1")
        elif self.player2_point >= 3 and self.player1_point < 3:
            return print("Winner player2")

    def display_score_print(self):
        text = f"""
        Match:
        Player 1: {self.player1_point}
        Player 2: {self.player2_point}"""
        return print(text)
