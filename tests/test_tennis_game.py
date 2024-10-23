import pytest

from tests.conftest import TennisScoreUpdater


class TestTennisGame:
    """
    Тестовый класс для проверки функционала класса TennisGame.
    """

    @pytest.mark.parametrize(
        "score_point, res",
        [
            (3, True),
            (2, False),
            (0, False),
        ]
    )
    def test_score_40_40(self, score_point: int, res: bool, create_match):
        """
        Тест проверяет, установилось ли состояние "deuce" (счёт 40:40) при заданных очках для игроков.
        Если оба игрока имеют 3 очка (40:40), должен быть активирован "deuce".

        :param score_point: Количество очков для обоих игроков, чтобы проверить переход в "deuce".
        :param res: Ожидаемый результат — True, если deuce активен, иначе False.
        :param create_match: Фикстура для создания матча с начальной установкой игры.
        """
        tennis = create_match
        tennis.__game.reset_points()  # Сброс очков перед тестом
        TennisScoreUpdater().add_score_players(score_point, tennis)  # Добавление очков обоим игрокам
        assert tennis.__game.deuce is res

    @pytest.mark.parametrize(
        "score_point, score_player, player1_point, player2_point, res",
        [
            (3, 1, 1, 0, "AD"),
            (3, 1, 0, 1, "AD"),
        ]
    )
    def test_deuce_state(self, score_point: int, score_player: int, player1_point: int,
                         player2_point: int, res: str, create_match):
        """
        Тест проверяет переход в состояние "Advantage" после "deuce" (40:40).
        Если оба игрока на "deuce", и один из них набирает очко, он должен перейти в состояние "Advantage".

        :param score_point: Очки, которые нужно установить для состояния "deuce".
        :param score_player: Количество очков, которые игрок набирает после "deuce".
        :param player1_point: Текущее количество очков игрока 1.
        :param player2_point: Текущее количество очков игрока 2.
        :param res: Ожидаемый результат — состояние "Advantage" для одного из игроков.
        :param create_match: Фикстура для создания матча с начальной установкой игры.
        """
        tennis = create_match
        tennis.__game.reset_points()
        TennisScoreUpdater().add_score_players(score_point, tennis)  # Установка состояния "deuce"
        TennisScoreUpdater().add_score_player(player1_point, player2_point, score_player, tennis)  # Добавление очков
        assert (tennis.__game.SCORE_MAPPING[tennis.__game.player1_point] == res
                or tennis.__game.SCORE_MAPPING[tennis.__game.player2_point] == res)

    @pytest.mark.parametrize(
        "score_point, res",
        [
            (4, "40"),
        ]
    )
    def test_return_to_deuce_after_advantage(self, score_point: int, res: str, create_match):
        """
        Тест проверяет, возвращается ли игра в состояние "deuce" после того, как игрок был в состоянии "Advantage",
        но проиграл очко. После потери преимущества ("Advantage") игра должна вернуться в состояние "deuce".

        :param score_point: Очки, которые нужно добавить для выхода из состояния "Advantage" обратно в "deuce".
        :param res: Ожидаемый результат — состояние "40:40" (deuce) для обоих игроков.
        :param create_match: Фикстура для создания матча с начальной установкой игры.
        """
        tennis = create_match
        tennis.__game.reset_points()
        TennisScoreUpdater().add_score_players(score_point, tennis)
        assert (tennis.__game.SCORE_MAPPING[tennis.__game.player1_point]
                and tennis.__game.SCORE_MAPPING[tennis.__game.player2_point])

    @pytest.mark.parametrize(
        "score_point, score_player, player1_point, player2_point, res",
        [
            (3, 2, 1, 0, 1),
            (3, 2, 0, 1, 1),
        ]
    )
    def test_deuce_wins_game(self, score_point: int, score_player: int, player1_point: int,
                             player2_point: int, res: str, create_match):
        """
        Тест проверяет, выигрывает ли игрок игру после состояния "deuce" (40:40) при переходе в "Advantage".

        :param score_point: Количество очков для обоих игроков, чтобы установить состояние "deuce".
        :param score_player: Очки, которые один из игроков набирает после состояния "deuce".
        :param player1_point: Начальное количество очков игрока 1 перед добавлением очков.
        :param player2_point: Начальное количество очков игрока 2 перед добавлением очков.
        :param res: Ожидаемый результат — победа игрока с состоянием "Advantage" (счёт должен увеличиться на 1).
        :param create_match: Фикстура для создания матча с начальной установкой игры.
        """
        tennis = create_match
        tennis.__game.reset_points()
        TennisScoreUpdater().add_score_players(score_point, tennis)  # Установка состояния "deuce"
        TennisScoreUpdater().add_score_player(player1_point, player2_point, score_player, tennis)  # Добавление очков
        assert (tennis.tennis_set.player1_point == res
                or tennis.tennis_set.player2_point == res)

    @pytest.mark.parametrize(
        "player1_point, player2_point, score_point, res",
        [
            (1, 0, 4, 1),
            (0, 1, 4, 1)
        ]
    )
    def test_player_wins_game(self, player1_point: int, player2_point: int, score_point: int, res: int, create_match):
        """
        Тест проверяет, выигрывает ли игрок игру при достижении 4 очков, в зависимости от стартовых условий.
        Игра завершается, если один из игроков набирает 4 очка, и результат записывается в счёт сета.

        :param player1_point: Начальные очки для игрока 1.
        :param player2_point: Начальные очки для игрока 2.
        :param score_point: Количество очков, которое нужно добавить для завершения игры.
        :param res: Ожидаемый результат — счёт очков победителя (игрок 1 или игрок 2).
        :param create_match: Фикстура для создания матча с начальной установкой игры.
        """
        tennis = create_match
        tennis.__game.reset_points()
        TennisScoreUpdater().add_score_player(player1_point, player2_point, score_point, tennis)
        assert tennis.tennis_set.player1_point == res or tennis.tennis_set.player2_point == res
