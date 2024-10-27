import pytest

from tests.conftest import TennisScoreUpdater


class TestTennisGame:
    """
    Тестовый класс для проверки функционала класса TennisGame.
    """

    @pytest.mark.parametrize(
        "iterations, res",
        [
            (4, '40'),
        ]
    )
    def test_score_40_40(self, iterations: int, res: bool, create_match):
        """
        Тест проверяет, возвращается ли игра в состояние "deuce" после того, как игрок был в состоянии "Advantage",
        но проиграл очко. После потери преимущества ("Advantage") игра должна вернуться в состояние "deuce".
        """
        TennisScoreUpdater().add_score_players(iterations, create_match)
        score = create_match.to_dict()
        score_player1 = score['test1']['game_score']
        score_player2 = score['test2']['game_score']
        assert score_player1 == res
        assert score_player2 == res

    @pytest.mark.parametrize(
        "iterations, iterations_one_player, player_point, res",
        [
            (3, 1, 1, "AD"),
            (3, 1, 2, "AD"),
        ]
    )
    def test_deuce_state(self, iterations: int, iterations_one_player: int, player_point: int,
                         res: str, create_match):
        """
        Тест проверяет переход в состояние "Advantage" после "deuce" (40:40).
        Если оба игрока на "deuce", и один из них набирает очко, он должен перейти в состояние "Advantage".

        """
        TennisScoreUpdater().add_score_players(iterations, create_match)
        TennisScoreUpdater().add_score_player(iterations_one_player, player_point, create_match)
        score = create_match.to_dict()
        if player_point == 1:
            score_player = score['test1']['game_score']
            assert score_player == res
        elif player_point == 2:
            score_player = score['test2']['game_score']
            assert score_player == res

    @pytest.mark.parametrize(
        "iterations, iterations_one_player, player_point, res",
        [
            (3, 2, 1, 1),
            (3, 2, 2, 1),
        ]
    )
    def test_deuce_wins_game(self, iterations: int, iterations_one_player: int, player_point: int,
                             res: str, create_match):
        """
        Тест проверяет, выигрывает ли игрок игру после состояния "deuce" (40:40) при переходе в "Advantage".
        """
        TennisScoreUpdater().add_score_players(iterations, create_match)
        TennisScoreUpdater().add_score_player(iterations_one_player, player_point, create_match)
        score = create_match.to_dict()
        if player_point == 1:
            score_player = score['test1']['set_score']
            assert score_player == res
        elif player_point == 2:
            score_player = score['test2']['set_score']
            assert score_player == res

    @pytest.mark.parametrize(
        "iterations_one_player, player_point, res",
        [
            (4, 1, 1),
            (4, 2, 1),
        ]
    )
    def test_player_wins_game(self, iterations_one_player: int, player_point: int,
                              res: str, create_match):
        """
        Тест проверяет, выигрывает ли игрок игру при достижении 4 очков, в зависимости от стартовых условий.
        Игра завершается, если один из игроков набирает 4 очка, и результат записывается в счёт сета.
        """
        TennisScoreUpdater().add_score_player(iterations_one_player, player_point, create_match)
        score = create_match.to_dict()
        if player_point == 1:
            score_player = score['test1']['set_score']
            assert score_player == res
        elif player_point == 2:
            score_player = score['test2']['set_score']
            assert score_player == res
