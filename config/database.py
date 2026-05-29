"""Configuracion de base de datos con SQLAlchemy.

Soporta SQLite para desarrollo local y MySQL/PostgreSQL para produccion en RDS.
La conexion se define mediante la variable de entorno DATABASE_URL.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///sicei.db")

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def init_db():
    """Crea todas las tablas definidas en los modelos."""
    Base.metadata.create_all(bind=engine)


def get_session():
    """Retorna una nueva sesion de base de datos.

    Returns:
        Session: Sesion de SQLAlchemy lista para usar.
    """
    return SessionLocal()
