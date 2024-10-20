from src.dao.player_dao import PlayerDao


class PlayerService:
    def __init__(self):
        self.player_dao = PlayerDao()

    def get_player(self, player: str):
        if self.is_player(player):
            return self.player_dao.get_player(player)
        return self.save_player(player)

    def get_player_by_id(self, player_id: int):
        player = self.player_dao.get_player_by_id(player_id)
        return player

    def save_player(self, player: str):
        self.player_dao.insert_player(player)
        return self.player_dao.get_player(player)

    def is_player(self, name):
        """ Проверка игрока есть ли он в БД """
        if self.player_dao.get_player(name):
            return True
        return False
