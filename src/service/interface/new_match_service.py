from abc import ABC, abstractmethod

from src.dto import MatchDTO, PlayersDTO


class NewMatchService(ABC):
    @abstractmethod
    def start_match(self, players: PlayersDTO) -> MatchDTO:
        pass
