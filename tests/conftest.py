import pytest

from src.service.tennis import Tennis


@pytest.fixture()
def create_match():
    match = Tennis()
    return match


class TennisScoreUpdater:
    def add_score_players(self, point: int, match: Tennis):
        tennis = match
        for _ in range(point):
            tennis.match.update_point(1, 0)
            tennis.match.update_point(0, 1)

    def add_score_player(self, player1_point: int, player2_point: int, point: int, match: Tennis):
        tennis = match
        for _ in range(point):
            tennis.match.update_point(player1_point, player2_point)

