import pytest

from tests.conftest import TennisScoreUpdater


class TestTennisSet:
    """
    Тестовый класс для проверки функционала класса TennisSet.
    """

    @pytest.mark.parametrize(
        "score_point, player1_point, player2_point, res",
        [
            (18, 1, 0, True),
            (18, 0, 1, True),
        ]
    )
    def test_tie_break_state(self, score_point: int, player1_point: int,
                             player2_point: int, res: bool, create_match):
        """
        Тест проверяет, активируется ли тай-брейк при достижении счёта 6:6 в сете.

        :param score_point: Количество очков, необходимое для активации тай-брейка.
        :param player1_point: Начальное количество очков игрока 1 перед тай-брейком.
        :param player2_point: Начальное количество очков игрока 2 перед тай-брейком.
        :param res: Ожидаемый результат — активация тай-брейка (True).
        :param create_match: Фикстура для создания матча с начальной установкой игры.
        """
        tennis = create_match
        tennis.__game.reset_points()  # Сброс очков перед тестом
        TennisScoreUpdater().add_score_set(score_point, tennis)  # Установка необходимого счёта для тай-брейка
        assert tennis.tennis_set.tie_break_flag == res

    @pytest.mark.parametrize(
        "score_point, score_player, player1_point, player2_point, res",
        [
            (18, 7, 1, 0, 1),
            (18, 7, 0, 1, 1),
        ]
    )
    def test_tie_break_winner(self, score_point: int, score_player: int, player1_point: int,
                              player2_point: int, res: int, create_match):
        """
        Тест проверяет, определяется ли победитель в тай-брейке при достижении 7 очков одним из игроков.
        После активации тай-брейка, первый игрок, который наберёт 7 очков при разнице минимум в 2 очка,
        становится победителем.

        :param score_point: Количество очков, необходимое для активации тай-брейка.
        :param score_player: Очки, набранные победителем тай-брейка.
        :param player1_point: Начальное количество очков игрока 1 перед тай-брейком.
        :param player2_point: Начальное количество очков игрока 2 перед тай-брейком.
        :param res: Ожидаемый результат — победитель (игрок 1 или игрок 2).
        :param create_match: Фикстура для создания матча с начальной установкой игры.
        """
        tennis = create_match
        tennis.__game.reset_points()
        TennisScoreUpdater().add_score_set(score_point, tennis)
        TennisScoreUpdater().add_score_player(player1_point, player2_point, score_player, tennis)
        assert tennis.__match.player1_point == res or tennis.__match.player2_point == res

    @pytest.mark.parametrize(
        "score_point, score_player, player1_point, player2_point, res",
        [
            (18, 7, 1, 0, False),
            (18, 7, 0, 1, False),
        ]
    )
    def test_tie_break_not_winner(self, score_point: int, score_player: int, player1_point: int,
                                  player2_point: int, res: bool, create_match):
        """
        Тест проверяет, что игроки не выигрывают сет, если они ещё не набрали достаточную разницу в очках в тай-брейке.
        Если оба игрока находятся в состоянии тай-брейка, но ещё не достигли 7 очков с разницей в 2 очка,
        сет не должен завершиться. Тест проверяет, что победа не засчитана.

        :param score_point: Количество очков для активации тай-брейка.
        :param score_player: Очки, добавленные во время тай-брейка.
        :param player1_point: Начальное количество очков игрока 1 перед тай-брейком.
        :param player2_point: Начальное количество очков игрока 2 перед тай-брейком.
        :param res: Ожидаемый результат — отсутствие победителя (False).
        :param create_match: Фикстура для создания матча с начальной установкой игры.
        """
        tennis = create_match
        tennis.__game.reset_points()
        TennisScoreUpdater().add_score_set(score_point, tennis)
        TennisScoreUpdater().add_score_players(score_player, tennis)
        assert tennis.tennis_set.player1_wins == res or tennis.tennis_set.player2_wins == res

    @pytest.mark.parametrize(
        "score_point, score_player, player1_point, player2_point, res",
        [
            (12, 8, 1, 0, 1),
            (12, 8, 0, 1, 1),
        ]
    )
    def test_set_winner(self, score_point: int, score_player: int, player1_point: int,
                        player2_point: int, res: int, create_match):
        """
        Тест проверяет определение победителя в сете при достижении 6 очков с разницей в 2 очка.
        Когда один из игроков набирает 6 очков и имеет разницу в 2 очка, он выигрывает сет.
        Этот тест проверяет, что сет корректно завершается и победитель определён.

        :param score_point: Количество очков, необходимое для завершения сета.
        :param score_player: Очки, набранные победителем сета.
        :param player1_point: Начальное количество очков игрока 1.
        :param player2_point: Начальное количество очков игрока 2.
        :param res: Ожидаемый результат — победитель сета (игрок 1 или игрок 2).
        :param create_match: Фикстура для создания матча с начальной установкой игры.
        """
        tennis = create_match
        tennis.__game.reset_points()
        TennisScoreUpdater().add_score_set(score_point, tennis)
        TennisScoreUpdater().add_score_player(player1_point, player2_point, score_player, tennis)
        assert tennis.__match.player1_point == res or tennis.__match.player2_point == res
