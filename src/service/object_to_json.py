import json


class ObjectToJsonDb:
    def dict_to_json(self, score_match: dict):
        score_match_json = json.dumps(score_match)
        return score_match_json

    def json_to_dict(self, score_match_json):
        score_match_dict = json.loads(score_match_json)
        return score_match_dict
