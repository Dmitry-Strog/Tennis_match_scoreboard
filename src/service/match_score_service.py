from src.service.data_access_or_storage.match_data import MatchData
from src.service.match_scoreboard_logic.tennis_scoreboard import ScoreboardTennis
from src.service.data_access_or_storage.match_service import MatchService
from src.service.object_to_json import ObjectToJsonDb
from src.service.data_access_or_storage.player_service import PlayerService


class MatchScoreService:
    def __init__(self):
        self.__player = PlayerService()
        self.__match = MatchService()
        self.__json_converter = ObjectToJsonDb()

    def play_match(self, uuid, point=None):
        scoreboard = self.__handle_match_progress(uuid)

        if point is None:
            return MatchData(uuid, scoreboard.to_dict())

        if self.__find_match(uuid).winner is not None:
            winner_id = self.__find_match(uuid).winner
            player_model = self.__player.get_player_by_id(winner_id)
            return MatchData(uuid, scoreboard.to_dict(), player_model.NAME)

        scoreboard.simulation_scoreboard(point)

        if scoreboard.winner_player is not None:
            winner = self.__player.get_player(scoreboard.winner_player.name)
            score_json = self.__json_converter.dict_to_json(scoreboard.to_dict())
            self.__match.update_match_score(uuid, score_json, winner.ID)

        score_json = self.__json_converter.dict_to_json(scoreboard.to_dict())
        self.__match.update_match_score(uuid, score_json)
        return MatchData(uuid, scoreboard.to_dict())

    def __handle_match_progress(self, uuid_match):
        match = self.__find_match(uuid_match)
        player1, player2 = self.__find_player(match.player1, match.player2)
        score_dict = self.__json_converter.json_to_dict(match.score)
        return ScoreboardTennis(player1.NAME, player2.NAME, score_dict)

    def __find_match(self, uuid):
        match_obj = self.__match.get_match_by_uuid(uuid)
        return match_obj

    def __find_player(self, player1_id, player2_id):
        player1 = self.__player.get_player_by_id(player1_id)
        player2 = self.__player.get_player_by_id(player2_id)
        return player1, player2
