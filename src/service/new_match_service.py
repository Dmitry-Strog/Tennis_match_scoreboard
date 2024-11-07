import json

from src.dao.match_dao import MatchDao
from src.dao.player_dao import PlayerDao
from src.models import PlayersModel
from src.service.data_access_or_storage.match_data import MatchData
from src.service.match_scoreboard_logic.tennis_scoreboard import ScoreboardTennis


class NewMatchService:
    def __init__(self):
        self.__player = PlayerDao()
        self.__match = MatchDao()

    def start_match(self, name_player1, name_player2):
        player1 = self.__find_player(name_player1)
        player2 = self.__find_player(name_player2)
        uuid = self.__create_match(player1, player2)

        scoreboard = ScoreboardTennis(player1.NAME, player2.NAME)

        score_json = json.dumps(scoreboard.to_dict())
        self.__match.update_match(uuid, score_json)
        return MatchData(uuid, scoreboard.to_dict())

    def __create_match(self, player1: PlayersModel, player2: PlayersModel):
        match_uuid = self.__match.insert_table_matches(player1.ID, player2.ID)
        return match_uuid

    def __find_player(self, name_player):
        player = self.__player.get_player(name_player)
        if player is None:
            self.__player.insert_player(name_player)
            return self.__player.get_player(name_player)
        return player
