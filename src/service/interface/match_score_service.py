from abc import ABC, abstractmethod

from src.dto import MatchDTO


class MatchScoreService(ABC):
    @abstractmethod
    def play_match(self, uuid: str, point: int = None) -> MatchDTO:
        pass
