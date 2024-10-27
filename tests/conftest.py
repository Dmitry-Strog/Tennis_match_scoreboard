import pytest
from src.service.match_scoreboard_logic.tennis_scoreboard import ScoreboardTennis


@pytest.fixture()
def create_match():
    """
    Фикстура для создания нового матча по теннису.

    """
    match = ScoreboardTennis("test1", "test2")
    return match


class TennisScoreUpdater:
    """
    Вспомогательный класс для обновления очков в матче по теннису.
    """

    def add_score_players(self, iterations: int, match: ScoreboardTennis):
        """
        Добавляет очки обоим игрокам поочередно.
        Этот метод полезен для тестирования сценариев, где оба игрока получают очки попеременно.
        """
        for _ in range(iterations):
            match.simulation_scoreboard(1)
            match.simulation_scoreboard(2)

    def add_score_set(self, iterations: int, match: ScoreboardTennis):
        """
        Добавляет очки в рамках одного сета для обоих игроков.
        """
        tennis = match
        for _ in range(iterations):
            tennis.simulation_scoreboard(1)
            tennis.simulation_scoreboard(1)
            tennis.simulation_scoreboard(2)
            tennis.simulation_scoreboard(2)

    def add_score_player(self, iterations: int, player_point: int, match: ScoreboardTennis):
        """
        Добавляет очки конкретному игроку.
        Полезно для тестирования сценариев, где один получает очки в определённой последовательности.
        """
        for _ in range(iterations):
            match.simulation_scoreboard(player_point)
