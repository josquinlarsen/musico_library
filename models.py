from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Piece model
class Piece(Base):
    """
    Piece table in database
    """

    __tablename__ = "pieces"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    composer = Column(String, index=True)
    instrumentation = Column(String, index=True)
    duration = Column(String, index=True)
