from src.service.data_access_or_storage.match_service import MatchService


class FinishedMatchService:
    def __init__(self):
        self.__match = MatchService()

    def get_match(self, name=None):
        list_match = self.__match.get_finished_match(name)
        return list_match

