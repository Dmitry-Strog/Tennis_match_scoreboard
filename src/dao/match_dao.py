import uuid

from sqlalchemy import update

from src.models import MatchesModel, sessions


class MatchDao:
    def insert_table_matches(self, player1: int, player2: int):
        match = MatchesModel(player1=player1, player2=player2)
        with sessions() as session:
            session.add(match)
            session.commit()
            return match.UUID

    def get_match_by_uuid(self, match_uuid: uuid.UUID) -> MatchesModel:
        with sessions() as session:
            match = session.query(MatchesModel).filter_by(UUID=str(match_uuid)).first()
            return match

    def update_match(self, uuid_match, score_json):
        with sessions() as session:
            match: MatchesModel = session.query(MatchesModel).filter(MatchesModel.UUID == uuid_match).one_or_none()
            match.score = score_json
            session.commit()
