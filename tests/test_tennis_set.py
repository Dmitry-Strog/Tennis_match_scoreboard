import pytest

from tests.conftest import TennisScoreUpdater


class TestTennisSet:
    """
    Тестовый класс для проверки функционала класса TennisSet.
    """

    @pytest.mark.parametrize(
        "iterations, iterations_one_player, player_point, res",
        [
            (18, 1, 1, 1),
            (18, 1, 2, 1),
        ]
    )
    def test_tie_break_state(self, iterations: int, iterations_one_player: int,
                             player_point: int, res: bool, create_match):
        """
        Тест проверяет, активируется ли тай-брейк при достижении счёта 6:6 в сете.
        """
        TennisScoreUpdater().add_score_set(iterations, create_match)
        TennisScoreUpdater().add_score_player(iterations_one_player, player_point, create_match)
        score = create_match.to_dict()
        if player_point == 1:
            score_player = score['test1']['tie_break_score']
            assert score_player == res
        elif player_point == 2:
            score_player = score['test2']['tie_break_score']
            assert score_player == res

    @pytest.mark.parametrize(
        "iterations, iterations_one_player, player_point, res",
        [
            (18, 7, 1, 1),
            (18, 7, 2, 1),
        ]
    )
    def test_tie_break_winner(self, iterations: int, iterations_one_player: int,
                              player_point: int, res: bool, create_match):
        """
        Тест проверяет, определяется ли победитель в тай-брейке при достижении 7 очков одним из игроков.
        После активации тай-брейка, первый игрок, который наберёт 7 очков при разнице минимум в 2 очка,
        становится победителем.
        """
        TennisScoreUpdater().add_score_set(iterations, create_match)
        TennisScoreUpdater().add_score_player(iterations_one_player, player_point, create_match)
        score = create_match.to_dict()
        if player_point == 1:
            score_player = score['test1']['match_score']
            assert score_player == res
        elif player_point == 2:
            score_player = score['test2']['match_score']
            assert score_player == res

    @pytest.mark.parametrize(
        "iterations, one_iteration, player_point, res",
        [
            (21, 1, 1, 7),
            (21, 1, 2, 7),
        ]
    )
    def test_tie_break_not_winner(self, iterations: int, one_iteration,
                                  player_point: int, res: bool, create_match):
        """
        Тест проверяет, что игроки не выигрывают сет, если они ещё не набрали достаточную разницу в очках в тай-брейке.
        Если оба игрока находятся в состоянии тай-брейка, но ещё не достигли 7 очков с разницей в 2 очка,
        сет не должен завершиться. Тест проверяет, что победа не засчитана.
        """
        TennisScoreUpdater().add_score_set(iterations, create_match)
        TennisScoreUpdater().add_score_players(one_iteration, create_match)
        score = create_match.to_dict()
        if player_point == 1:
            score_player = score['test1']['tie_break_score']
            assert score_player == res
        elif player_point == 2:
            score_player = score['test2']['tie_break_score']
            assert score_player == res
