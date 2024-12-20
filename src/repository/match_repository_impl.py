from sqlalchemy import or_
from sqlalchemy.orm import joinedload

from src.dto import MatchDTO
from src.exceptions import MatchNotFoundException
from src.models import MatchesModel, sessions
from src.repository.interface.match_repository import MatchRepository


class MatchRepositoryImpl(MatchRepository):
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
            if match is None:
                raise MatchNotFoundException
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

    def update_match(self, match: MatchDTO):
        with sessions() as session:
            current_match: MatchesModel = session.query(
                MatchesModel).filter(MatchesModel.UUID == match.uuid).one_or_none()
            current_match.score = match.score
            if match.winner is not None:
                current_match.winner = match.winner
            session.commit()

