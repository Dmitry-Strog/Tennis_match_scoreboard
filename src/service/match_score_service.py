from src.service.match_data import MatchData
from src.service.match_scoreboard_service.tennis_scoreboard import ScoreboardTennis
from src.service.match_service import MatchService
from src.service.object_to_json import ObjectToJsonDb
from src.service.player_service import PlayerService


class MatchScoreService:
    def __init__(self):
        self.player = PlayerService()
        self.match = MatchService()
        self.json_converter = ObjectToJsonDb()

    def play_match(self, uuid, point=None):
        match = self.find_match(uuid)
        player1, player2 = self.find_player(match.player1, match.player2)
        score_dict = self.json_converter.json_to_dict(match.score)
        scoreboard = ScoreboardTennis(player1.NAME, player2.NAME, score_dict)
        score_json = self.json_converter.dict_to_json(scoreboard.to_dict())
        if point is not None:
            self.match.update_match_score(uuid, score_json)
            return MatchData(uuid, score_json)
        return MatchData(uuid, score_dict)

    def find_match(self, uuid):
        match_obj = self.match.get_match(uuid)
        return match_obj

    def find_player(self, player1_id, player2_id):
        player1 = self.player.get_player_by_id(player1_id)
        player2 = self.player.get_player_by_id(player2_id)
        return player1, player2

# tmp = MatchScoreService()
# q = tmp.play_match("b3342984-2468-4e1e-a392-2d057bbe01df")
# print(type(q.score))
