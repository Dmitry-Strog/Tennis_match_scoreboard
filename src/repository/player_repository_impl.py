from sqlalchemy import select

from src.models import PlayersModel, sessions
from src.repository.interface.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    def get_player(self, name: str):
        """ Получение игрока из БД"""
        with sessions() as session:
            player = session.scalars(select(PlayersModel).filter_by(NAME=name)).one_or_none()
            return player

    def get_player_by_id(self, id: int):
        """ Получение игрока из БД"""
        with sessions() as session:
            player = session.scalars(select(PlayersModel).filter_by(ID=id)).one_or_none()
            return player

    def insert_player(self, name: str):
        """ Добавление игрока в БД"""
        player = PlayersModel(NAME=name)
        with sessions() as session:
            session.add(player)
            session.commit()
