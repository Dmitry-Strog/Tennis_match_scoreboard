from abc import ABC, abstractmethod

from src.match_data import MatchData


class NewMatchService(ABC):
    @abstractmethod
    def start_match(self, name_player1: str, name_player2: str) -> MatchData:
        pass
