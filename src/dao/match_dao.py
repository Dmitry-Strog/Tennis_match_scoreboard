import uuid

from src.models import PlayersModel, MatchesModel, sessions


class MatchDao:
    def insert_table_matches(self, player1: int, player2: int):
        match = MatchesModel(player1=player1, player2=player2)
        with sessions() as session:
            session.add(match)
            session.commit()
            session.refresh(match)
            return match.UUID

    def get_match_by_uuid(self, match_uuid: uuid.UUID) -> MatchesModel:
        with sessions() as session:
            match = session.query(MatchesModel).filter_by(UUID=str(match_uuid)).first()
            return match

    def update_match(self):
        pass