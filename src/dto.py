import json
from dataclasses import dataclass
from typing import Union, Dict, Any


@dataclass
class MatchDTO:
    uuid: str
    score: Union[Dict[str, Any], str]
    winner: str = None


@dataclass
class PlayersDTO:
    player_name_1: str
    player_name_2: str
