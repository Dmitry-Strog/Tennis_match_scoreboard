from sqlalchemy import or_
from sqlalchemy.orm import joinedload

from src.models import MatchesModel, sessions


class MatchDao:
    def insert_table_matches(self, player1: int, player2: int):
        match = MatchesModel(player1=player1, player2=player2)
        with sessions() as session:
            session.add(match)
            session.commit()
            return match.UUID

    def get_match_by_uuid(self, match_uuid: str) -> MatchesModel:
        with sessions() as session:
            match = session.query(MatchesModel).options(
                joinedload(MatchesModel.player1_rel),
                joinedload(MatchesModel.player2_rel),
                joinedload(MatchesModel.winner_rel),
            ).filter_by(UUID=str(match_uuid)).first()
            return match

    def get_finished_matches(self, name=None):
        with sessions() as session:
            matches = session.query(MatchesModel).options(
                joinedload(MatchesModel.player1_rel),
                joinedload(MatchesModel.player2_rel),
                joinedload(MatchesModel.winner_rel),
            ).filter(MatchesModel.winner != None)

            if name:
                matches = matches.filter(
                    or_(
                        MatchesModel.player1_rel.has(NAME=name),
                        MatchesModel.player2_rel.has(NAME=name)
                    )
                )
            return matches.all()

    def update_match(self, uuid_match, score_json, winner_id=None):
        with sessions() as session:
            match: MatchesModel = session.query(MatchesModel).filter(MatchesModel.UUID == uuid_match).one_or_none()
            match.score = score_json
            if winner_id is not None:
                match.winner = winner_id
            session.commit()
