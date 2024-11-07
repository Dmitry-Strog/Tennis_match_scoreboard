import json

from src.dao.match_dao import MatchDao
from src.dao.player_dao import PlayerDao
from src.service.data_access_or_storage.match_data import MatchData
from src.service.match_scoreboard_logic.tennis_scoreboard import ScoreboardTennis


class MatchScoreService:
    def __init__(self):
        self.__player = PlayerDao()
        self.__match = MatchDao()

    def play_match(self, uuid, point=None):
        scoreboard = self.__handle_match_progress(uuid)

        if point is None:
            return MatchData(uuid, scoreboard.to_dict())

        if self.__match.get_match_by_uuid(uuid).winner is not None:
            winner_id = self.__match.get_match_by_uuid(uuid).winner
            player_model = self.__player.get_player_by_id(winner_id)
            return MatchData(uuid, scoreboard.to_dict(), player_model.NAME)

        scoreboard.simulation_scoreboard(point)

        if scoreboard.winner_player is not None:
            winner_name = scoreboard.winner_player.name
            winner = self.__player.get_player(winner_name)
            score_json = json.dumps(scoreboard.to_dict())
            self.__match.update_match(uuid, score_json, winner.ID)
            return MatchData(uuid, scoreboard.to_dict(), winner.NAME)

        score_json = json.dumps(scoreboard.to_dict())
        self.__match.update_match(uuid, score_json)

        return MatchData(uuid, scoreboard.to_dict())

    def __handle_match_progress(self, uuid_match):
        match = self.__match.get_match_by_uuid(uuid_match)
        player1 = self.__player.get_player_by_id(match.player1)
        player2 = self.__player.get_player_by_id(match.player2)
        score_dict = json.loads(match.score)
        return ScoreboardTennis(player1.NAME, player2.NAME, score_dict)
