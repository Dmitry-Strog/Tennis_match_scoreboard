import json

from src.repository.interface.match_repository import MatchRepository
from src.repository.interface.player_repository import PlayerRepository
from src.models import PlayersModel
from src.dto import MatchDTO, PlayersDTO
from src.service.interface.new_match_service import NewMatchService
from src.service.match_scoreboard_logic.tennis_scoreboard import ScoreboardTennis


class NewMatchServiceImpl(NewMatchService):
    def __init__(self, player_repo: PlayerRepository, match_repo: MatchRepository):
        self.__player = player_repo
        self.__match = match_repo

    def start_match(self, players: PlayersDTO) -> MatchDTO:
        player1 = self.__find_player(players.player_name_1)
        player2 = self.__find_player(players.player_name_2)
        match_uuid = self.__create_match(player1, player2)

        scoreboard = ScoreboardTennis(player1.NAME, player2.NAME)

        self.__update_match_score(match_uuid, scoreboard.to_dict())
        return MatchDTO(match_uuid, scoreboard.to_dict())

    def __create_match(self, player1: PlayersModel, player2: PlayersModel):
        match_uuid = self.__match.insert_table_matches(player1.ID, player2.ID)
        return match_uuid

    def __find_player(self, name_player: str):
        player = self.__player.get_player(name_player)
        if player is None:
            self.__player.insert_player(name_player)
            return self.__player.get_player(name_player)
        return player

    def __update_match_score(self, match_uuid: str, score_data: dict):
        score_json = json.dumps(score_data)
        self.__match.update_match(MatchDTO(match_uuid, score_json))
