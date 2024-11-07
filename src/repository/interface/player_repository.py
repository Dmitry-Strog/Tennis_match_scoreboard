from abc import ABC, abstractmethod

from src.models import PlayersModel


class PlayerRepository(ABC):
    @abstractmethod
    def insert_player(self, name: str) -> None:
        pass

    @abstractmethod
    def get_player(self, name: str) -> PlayersModel:
        pass

    @abstractmethod
    def get_player_by_id(self, id: int) -> PlayersModel:
        pass
