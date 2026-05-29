"""Modelo Profesor con SQLAlchemy.

Define la tabla profesores y las operaciones CRUD usando sesiones de base de datos.
"""

from config.database import Base, get_session
from sqlalchemy import Column, Integer, String


class Profesor(Base):
    """Representa un profesor del sistema SICEI.

    Attributes:
        id (int): Identificador unico, auto-generado por la base de datos.
        numeroEmpleado (int): Numero de empleado del profesor.
        nombres (str): Nombres del profesor.
        apellidos (str): Apellidos del profesor.
        horasClase (int): Horas de clase asignadas al profesor.
    """

    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numeroEmpleado = Column(Integer, nullable=False)
    nombres = Column(String(255), nullable=False)
    apellidos = Column(String(255), nullable=False)
    horasClase = Column(Integer, nullable=False)

    def to_dict(self):
        """Convierte el profesor a un diccionario.

        Returns:
            dict: Representacion del profesor en formato diccionario.
        """
        return {
            "id": self.id,
            "numeroEmpleado": self.numeroEmpleado,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "horasClase": self.horasClase,
        }


def get_all():
    """Obtiene todos los profesores registrados.

    Returns:
        list[dict]: Lista de profesores en formato diccionario.
    """
    session = get_session()
    try:
        profesores = session.query(Profesor).all()
        return [profesor.to_dict() for profesor in profesores]
    finally:
        session.close()


def get_by_id(id):
    """Busca un profesor por su id.

    Args:
        id (int): Identificador del profesor a buscar.

    Returns:
        dict | None: Diccionario del profesor si existe, None en caso contrario.
    """
    session = get_session()
    try:
        profesor = session.get(Profesor, id)
        return profesor.to_dict() if profesor else None
    finally:
        session.close()


def create(data):
    """Crea un nuevo profesor y lo guarda en la base de datos.

    Args:
        data (dict): Datos del profesor con las llaves numeroEmpleado,
            nombres, apellidos y horasClase.

    Returns:
        dict: El profesor creado en formato diccionario, incluyendo el id
            generado por la base de datos.
    """
    session = get_session()
    try:
        profesor = Profesor(
            numeroEmpleado=data["numeroEmpleado"],
            nombres=data["nombres"],
            apellidos=data["apellidos"],
            horasClase=data["horasClase"],
        )
        session.add(profesor)
        session.commit()
        session.refresh(profesor)
        return profesor.to_dict()
    finally:
        session.close()


def update(id, data):
    """Actualiza los datos de un profesor existente.

    Args:
        id (int): Identificador del profesor a actualizar.
        data (dict): Nuevos datos del profesor.

    Returns:
        dict | None: Diccionario del profesor actualizado, None si no existe.
    """
    session = get_session()
    try:
        profesor = session.get(Profesor, id)
        if not profesor:
            return None
        profesor.numeroEmpleado = data.get(
            "numeroEmpleado", profesor.numeroEmpleado
        )
        profesor.nombres = data.get("nombres", profesor.nombres)
        profesor.apellidos = data.get("apellidos", profesor.apellidos)
        profesor.horasClase = data.get("horasClase", profesor.horasClase)
        session.commit()
        session.refresh(profesor)
        return profesor.to_dict()
    finally:
        session.close()


def delete(id):
    """Elimina un profesor de la base de datos.

    Args:
        id (int): Identificador del profesor a eliminar.

    Returns:
        bool: True si se elimino, False si no se encontro.
    """
    session = get_session()
    try:
        profesor = session.get(Profesor, id)
        if not profesor:
            return False
        session.delete(profesor)
        session.commit()
        return True
    finally:
        session.close()
