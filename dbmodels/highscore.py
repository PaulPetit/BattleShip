from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class HighScore(Base):
    __tablename__ = 'HighScores'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(String)

    def __repr__(self):
        return "<HighScore(name='%s', score='%s')>" % (self.name, self.score)
