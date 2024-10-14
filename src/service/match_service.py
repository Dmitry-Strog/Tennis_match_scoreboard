from src.dao.match_dao import MatchDao
from src.models import PlayersModel


class MatchService:
    def __init__(self):
        self.match_dao = MatchDao()

    def create_match(self, player1: PlayersModel, player2: PlayersModel):
        match_uuid = self.match_dao.insert_table_matches(player1.ID, player2.ID)
        return match_uuid

    # def get_match(self, match_uuid):
    #     pass

    # def update_match_score(self, player: str):
    #     pass

    # def is_match(self, name):
    #     """ Проверка игрока есть ли он в БД """
    #     pass
