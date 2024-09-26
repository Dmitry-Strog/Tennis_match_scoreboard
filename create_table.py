from sqlalchemy import select

from src.models.database import engine, Base, sessions
from src.models.models import PlayersModel, MatchesModel


class CreateTableDatabase:

    def create_table(self):
        engine.echo = False
        Base.metadata.drop_all(engine)
        engine.echo = True
        Base.metadata.create_all(engine)

    def insert_table_players(self):
        player1 = PlayersModel(NAME="Dima")
        player2 = PlayersModel(NAME="Nikita")
        with sessions() as session:
            session.add(player1)
            session.add(player2)
            session.commit()

    def insert_table_matches(self):
        match = MatchesModel(player1=1, player2=2, winner=1, score="WIN")
        with sessions() as session:
            session.add(match)
            session.commit()

    def select_table(self):
        with sessions() as session:
            player = session.scalars(select(PlayersModel)).all()
            print(player)


create = CreateTableDatabase()
create.create_table()
create.insert_table_players()
create.insert_table_matches()
create.select_table()
