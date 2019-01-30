from dbmodels.highscore import HighScore
from models.engine import Engine
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_stuff():
    servername = "DESKTOP-JUKRIMR\MSSQLSERVER01"
    dbname = "BattleShip"
    engine = create_engine(
        'mssql+pyodbc://@' + servername + '/' + dbname + '?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    # connection = engine.connect()
    # ret = connection.execute("select * from HighScores")
    # for id, name, score in ret:
    #     print(name)
    Session = sessionmaker(bind=engine)
    session = Session()

    hs = HighScore()
    hs.name = "tata"
    hs.score = "118218"

    session.add(hs)
    session.commit()

    for instance in session.query(HighScore).order_by(HighScore.id):
        print(instance.name, instance.score)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='BattleShip Game')
    parser.add_argument('-i', help='Init DB', action="store_true")

    args = parser.parse_args()
    # print(args)

    if args.i:
        db_stuff()
    else:
        engine = Engine()
        engine.start()
        while engine.is_running:
            engine.turn()

        print("Fin du jeu !")
