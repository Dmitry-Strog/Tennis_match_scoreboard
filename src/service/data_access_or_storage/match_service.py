from src.dao.match_dao import MatchDao
from src.models import PlayersModel


class MatchService:
    def __init__(self):
        self.__match_dao = MatchDao()

    def create_match(self, player1: PlayersModel, player2: PlayersModel):
        match_uuid = self.__match_dao.insert_table_matches(player1.ID, player2.ID)
        return match_uuid

    def update_match_score(self, uuid_match, score_json, winner=None):
        if winner is None:
            self.__match_dao.update_match(uuid_match, score_json)
        else:
            self.__match_dao.update_match(uuid_match, score_json, winner)

    def get_match_by_uuid(self, match_uuid):
        match = self.__match_dao.get_match_by_uuid(match_uuid)
        return match

    def get_match_winner_id(self, match_uuid):
        match = self.__match_dao.get_match_by_uuid(match_uuid)
        return match