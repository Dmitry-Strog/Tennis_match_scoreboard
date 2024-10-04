from src.service.tennis_game import TennisGame
from src.service.tennis_tie_break import TieBreak


class TennisSet:
    """
    Класс TennisSet представляет собой один сет в теннисном матче. Он управляет очками игроков,
    состоянием сета и переходом на тай-брейк при необходимости.
    """
    def __init__(self, game: TennisGame, tie_break: TieBreak):
        """
        :param game: Экземпляр класса TennisGame для управления обычной игрой.
        :param tie_break: Экземпляр класса TieBreak для управления тай-брейком.
        """
        self.player1_point: int = 0
        self.player2_point: int = 0
        self.game: TennisGame = game
        self.tie_break: TieBreak = tie_break
        self.tie_break_flag: bool = False
        self.player1_wins: bool = False
        self.player2_wins: bool = False

    def update_point(self, player_1: int, player_2: int):
        """
        Обновляет очки игроков, выбирая между обычной игрой и тай-брейком, в зависимости от состояния игры.
        :param player_1: Очко для игрока 1 (1 - если он выиграл очко, 0 - иначе).
        :param player_2: Очко для игрока 2 (1 - если он выиграл очко, 0 - иначе).
        """
        if self.tie_break_flag:
            self.update_tie_break_point(player_1, player_2)
        else:
            self.update_game_point(player_1, player_2)

    def update_game_point(self, player_1: int, player_2: int):
        """
        Обновляет очки для обычной игры и проверяет, завершилась ли игра победой одного из игроков.
        """
        self.game.update_point(player_1, player_2)
        if self.game.is_end_game():
            self.add_game_point(self.game.get_winner())
            self.game.reset_points()

    def update_tie_break_point(self, player_1: int, player_2: int):
        """
        Обновляет очки для тай-брейка и проверяет, завершился ли тай-брейк победой одного из игроков.
        """
        self.tie_break.update_point(player_1, player_2)
        if self.tie_break.is_end_game():
            self.set_tie_break_winner(self.tie_break.get_winner())
            self.tie_break.reset_points()

    def add_game_point(self, winner: str):
        """
        Добавляет очко за выигранную игру игроку, который победил в обычной игре.
        :param winner: Победитель игры ("Player1" или "Player2").
        """
        if winner == "Player1":
            self.player1_point += 1
        elif winner == "Player2":
            self.player2_point += 1
        self.check_point()

    def set_tie_break_winner(self, winner: str):
        """
        Устанавливает победителя сета на основе результата тай-брейка.
        :param winner: Победитель тай-брейка ("Player1" или "Player2").
        """
        if winner == "Player1":
            self.player1_wins = True
        elif winner == "Player2":
            self.player2_wins = True

    def check_point(self):
        """
        Проверяет, достиг ли один из игроков условий для победы в сете.
        """
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

    def is_end_game(self) -> bool:
        """
        Проверяет, завершён ли сет.
        :return: True, если один из игроков выиграл сет, иначе False.
        """
        return self.player1_wins or self.player2_wins

    def get_winner(self) -> str:
        """
        Возвращает победителя сета, если сет завершён.
        """
        if self.is_end_game():
            if self.player1_wins:
                return "Player1"
            elif self.player2_wins:
                return "Player2"

    def reset_points(self):
        """
        Сбрасывает очки и состояние сета (включая тай-брейк флаг) для начала нового сета.
        """
        self.player1_point = 0
        self.player2_point = 0
        self.player1_wins = False
        self.player2_wins = False
        self.tie_break_flag: bool = False

    def display_score_print(self):
        """
        Выводит текущий счёт сета для обоих игроков.
        """
        text = f"""
        Set:
        Player 1: {self.player1_point}
        Player 2: {self.player2_point}"""
        return print(text)
