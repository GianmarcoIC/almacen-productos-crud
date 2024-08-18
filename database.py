import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False)

def init_db():
    database_url = os.getenv('DATABASE_URL')
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    return engine
