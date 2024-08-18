import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definición de la base de datos
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False)

# Función para inicializar la base de datos
def init_db():
    database_url = os.getenv('postgresql://postgres:ibBPwUDErJYUSAtGTlOjncsqBDZnBFEa@autorack.proxy.rlwy.net:25567/railway')  # Obtiene la URL de la base de datos desde las variables de entorno
    engine = create_engine(database_url)  # Crea una instancia del motor de la base de datos
    Base.metadata.create_all(engine)  # Crea todas las tablas en la base de datos
    return engine
