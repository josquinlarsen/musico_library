from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///library.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
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


# Create the database table
Base.metadata.create_all(bind=engine)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
