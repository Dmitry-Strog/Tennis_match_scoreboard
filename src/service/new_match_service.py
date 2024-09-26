from src.dao.match_dao import MatchDao
from src.dao.player_dao import PlayerDao
from src.models import PlayersModel


class NewMatchService:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.player_dao = PlayerDao()
        self.match_dao = MatchDao()

    def create_match(self, data_players: dict):
        player1, player2 = data_players.values()
        self.player1: PlayersModel = self.find_or_create_player(player1[0])
        self.player2: PlayersModel = self.find_or_create_player(player2[0])
        self.match_dao.insert_table_matches(self.player1.ID, self.player2.ID, self.player1.ID)

    def find_or_create_player(self, player: str):
        """ Возвращается игрок если он есть в БД
        или создает игрока и возвращает"""
        if self.check_player(player):
            return self.player_dao.get_player(player)
        self.player_dao.insert_player(player)
        return self.player_dao.get_player(player)

    def check_player(self, name):
        """ Проверка игрока есть ли он в БД """
        if self.player_dao.get_player(name):
            return True
        return False
