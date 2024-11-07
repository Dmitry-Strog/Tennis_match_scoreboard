from abc import ABC, abstractmethod

from src.match_data import MatchData


class MatchScoreService(ABC):
    @abstractmethod
    def play_match(self, uuid: str, point: int = None) -> MatchData:
        pass
