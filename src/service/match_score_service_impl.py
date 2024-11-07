import json

from src.models import MatchesModel
from src.repository.interface.match_repository import MatchRepository
from src.repository.interface.player_repository import PlayerRepository
from src.match_data import MatchData
from src.service.interface.match_score_service import MatchScoreService
from src.service.match_scoreboard_logic.tennis_scoreboard import ScoreboardTennis


class MatchScoreServiceImpl(MatchScoreService):
    def __init__(self, player_repo: PlayerRepository, match_repo: MatchRepository):
        self.__player = player_repo
        self.__match = match_repo

    def play_match(self, uuid: str, point: int = None) -> MatchData:
        match: MatchesModel = self.__match.get_match_by_uuid(uuid)
        scoreboard = self.__initialize_scoreboard(match)

        if point is None:
            return MatchData(uuid, scoreboard.to_dict())

        if match.winner is not None:
            winner_name = match.winner_rel.NAME
            return MatchData(uuid, scoreboard.to_dict(), winner_name)

        scoreboard.simulation_scoreboard(point)

        if scoreboard.winner_player is not None:
            return self.__finalize_match_with_winner(uuid, scoreboard)

        score_json = json.dumps(scoreboard.to_dict())
        self.__match.update_match(uuid, score_json)

        return MatchData(uuid, scoreboard.to_dict())

    def __initialize_scoreboard(self, match: MatchesModel) -> ScoreboardTennis:
        player1 = self.__player.get_player_by_id(match.player1)
        player2 = self.__player.get_player_by_id(match.player2)
        score_dict = json.loads(match.score)
        return ScoreboardTennis(player1.NAME, player2.NAME, score_dict)

    def __finalize_match_with_winner(self, uuid: str, scoreboard: ScoreboardTennis) -> MatchData:
        winner_name = scoreboard.winner_player.name
        winner = self.__player.get_player(winner_name)
        score_json = json.dumps(scoreboard.to_dict())
        self.__match.update_match(uuid, score_json, winner.ID)
        return MatchData(uuid, scoreboard.to_dict(), winner.NAME)
