import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = db.create_engine(
    "postgresql://username:password@localhost:5432/company"
)
SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
