from sqlalchemy import select

from src.models import PlayersModel, MatchesModel, sessions


class MatchDao:
    def insert_table_matches(self, player1:int, player2:int, winner:int):
        match = MatchesModel(player1=player1, player2=player2, winner=winner, score="WIN")
        with sessions() as session:
            session.add(match)
            session.commit()
