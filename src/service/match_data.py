from dataclasses import dataclass


@dataclass
class MatchData:
    uuid: str
    score: dict
