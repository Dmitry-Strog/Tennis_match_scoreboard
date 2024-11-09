import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Annotated

from src.models.database import Base, str_50, str_36

int_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
player_id = Annotated[int, mapped_column(ForeignKey("players.ID", ondelete="CASCADE"))]


class PlayersModel(Base):
    __tablename__ = "players"
    ID: Mapped[int_pk]
    NAME: Mapped[str_50] = mapped_column(nullable=False, unique=True, index=True)

    def __repr__(self):
        return f"PlayersModel{self.ID}:{self.NAME}"


class MatchesModel(Base):
    __tablename__ = "matches"
    ID: Mapped[int_pk]
    UUID: Mapped[uuid.UUID] = mapped_column(CHAR(36), unique=True, default=lambda: str(uuid.uuid4()))
    player1: Mapped[int] = mapped_column(ForeignKey("players.ID", ondelete="CASCADE"))
    player2: Mapped[int] = mapped_column(ForeignKey("players.ID", ondelete="CASCADE"))
    winner: Mapped[int] = mapped_column(ForeignKey("players.ID", ondelete="CASCADE"), nullable=True)
    score: Mapped[int] = mapped_column(String(256), nullable=True)

    player1_rel: Mapped["PlayersModel"] = relationship("PlayersModel", foreign_keys=[player1])
    player2_rel: Mapped["PlayersModel"] = relationship("PlayersModel", foreign_keys=[player2])
    winner_rel: Mapped["PlayersModel"] = relationship("PlayersModel", foreign_keys=[winner])

    def __repr__(self):
        return (f"MatchesModel {self.ID}: {self.UUID}, "
                f"Player 1: {self.player1_rel.NAME}, Player 2: {self.player2_rel.NAME}, "
                f"Winner: {self.winner_rel}, Score: {self.score}")
