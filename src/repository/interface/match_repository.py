from abc import ABC, abstractmethod

from src.dto import MatchDTO
from src.models import MatchesModel


class MatchRepository(ABC):
    @abstractmethod
    def insert_table_matches(self, player1: int, player2: int) -> MatchesModel.UUID:
        pass

    @abstractmethod
    def get_match_by_uuid(self, match_uuid: str) -> MatchesModel:
        pass

    @abstractmethod
    def get_finished_matches(self, name=None) -> list[MatchesModel]:
        pass

    @abstractmethod
    def update_match(self, match: MatchDTO) -> None:
        pass
