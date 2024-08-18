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
    database_url = os.getenv('postgresql://postgres:ibBPwUDErJYUSAtGTlOjncsqBDZnBFEa@autorack.proxy.rlwy.net:25567/railway')
    
    # Verifica si la URL está correctamente cargada
    if not database_url:
        raise ValueError("DATABASE_URL no está configurada. Por favor, revisa las variables de entorno.")

    # Intentar crear el engine con la URL proporcionada
    try:
        engine = create_engine(database_url, echo=True)
        Base.metadata.create_all(engine)
        return engine
    except Exception as e:
        raise ValueError(f"Error al crear el engine de la base de datos: {str(e)}")

# Inicializa la base de datos y crea la sesión
engine = init_db()
Session = sessionmaker(bind=engine)
session = Session()
