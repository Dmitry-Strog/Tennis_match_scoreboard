from src.service.data_access_or_storage.match_data import MatchData
from src.service.match_scoreboard_logic.tennis_scoreboard import ScoreboardTennis
from src.service.data_access_or_storage.match_service import MatchService
from src.service.object_to_json import ObjectToJsonDb
from src.service.data_access_or_storage.player_service import PlayerService


class NewMatchService:
    def __init__(self):
        self.__player = PlayerService()
        self.__match = MatchService()
        self.__json_converter = ObjectToJsonDb()

    def start_match(self, name_player1, name_player2):
        player1, player2 = self.__find_player(name_player1, name_player2)
        uuid = self.__find_match(player1, player2)
        scoreboard = ScoreboardTennis(player1.NAME, player2.NAME)
        score_json = self.__json_converter.dict_to_json(scoreboard.to_dict())
        self.__match.update_match_score(uuid, score_json)
        return MatchData(uuid, score_json)

    def __find_match(self, player1, player2):
        match_uuid = self.__match.create_match(player1, player2)
        return match_uuid

    def __find_player(self, name_player1, name_player2):
        player1 = self.__player.get_player(name_player1)
        player2 = self.__player.get_player(name_player2)
        return player1, player2
