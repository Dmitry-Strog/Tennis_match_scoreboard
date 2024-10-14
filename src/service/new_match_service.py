from src.service.match_data import MatchData
from src.service.match_scoreboard_service.tennis_scoreboard import ScoreboardTennis
from src.service.match_service import MatchService
from src.service.player_service import PlayerService


class NewMatchService:
    def __init__(self):
        self.player = PlayerService()
        self.match = MatchService()

    def start_match(self, name_player1, name_player2):
        player1, player2 = self.find_player(name_player1, name_player2)
        uuid = self.find_match(player1, player2)
        scoreboard = ScoreboardTennis(player1.NAME, player2.NAME)
        return MatchData(uuid, scoreboard.to_dict())

    def find_match(self, player1, player2):
        match_uuid = self.match.create_match(player1, player2)
        return match_uuid

    def find_player(self, name_player1, name_player2):
        player1 = self.player.get_player(name_player1)
        player2 = self.player.get_player(name_player2)
        return player1, player2
