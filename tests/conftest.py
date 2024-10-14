import pytest
from src.service.match_scoreboard_service.tennis_scoreboard import ScoreboardTennis


@pytest.fixture()
def create_match():
    """
    Фикстура для создания нового матча по теннису.
    :return: Новый экземпляр объекта Tennis.
    """
    match = ScoreboardTennis()
    return match


class TennisScoreUpdater:
    """
    Вспомогательный класс для обновления очков в матче по теннису.
    """

    def add_score_players(self, point: int, match: ScoreboardTennis):
        """
        Добавляет очки обоим игрокам поочередно.
        Этот метод полезен для тестирования сценариев, где оба игрока получают очки попеременно.

        :param point: Количество очков для каждого игрока.
        :param match: Экземпляр матча Tennis, в котором обновляются очки.
        """
        tennis = match
        for _ in range(point):
            tennis.match.update_point(1, 0)
            tennis.match.update_point(0, 1)

    def add_score_set(self, point: int, match: ScoreboardTennis):
        """
        Добавляет очки в рамках одного сета для обоих игроков.

        :param point: Количество обновлений счета
        :param match: Экземпляр матча Tennis, в котором обновляется счет.
        """
        tennis = match
        for _ in range(point):
            tennis.match.update_point(1, 0)
            tennis.match.update_point(1, 0)
            tennis.match.update_point(0, 1)
            tennis.match.update_point(0, 1)

    def add_score_player(self, player1_point: int, player2_point: int, point: int, match: ScoreboardTennis):
        """
        Добавляет очки конкретному игроку.
        Полезно для тестирования сценариев, где один получает очки в определённой последовательности.

        :param player1_point: Количество очков для игрока 1.
        :param player2_point: Количество очков для игрока 2.
        :param point: Количество обновлений счета.
        :param match: Экземпляр матча Tennis для обновления очков.
        """
        tennis = match
        for _ in range(point):
            tennis.match.update_point(player1_point, player2_point)
