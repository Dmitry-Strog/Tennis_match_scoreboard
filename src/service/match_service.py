from src.dao.match_dao import MatchDao
from src.models import PlayersModel


class MatchService:
    def __init__(self):
        self.match_dao = MatchDao()

    def create_match(self, player1: PlayersModel, player2: PlayersModel):
        match_uuid = self.match_dao.insert_table_matches(player1.ID, player2.ID)
        return match_uuid

    def update_match_score(self, uuid_match, score_json):
        self.match_dao.update_match(uuid_match, score_json)

    def get_match(self, match_uuid):
        match = self.match_dao.get_match_by_uuid(match_uuid)
        return match

    # def is_match(self, name):

    #     """ Проверка игрока есть ли он в БД """
    #     pass

