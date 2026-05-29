"""Modelo Alumno con SQLAlchemy.

Define la tabla alumnos y las operaciones CRUD usando sesiones de base de datos.
"""

from config.database import Base, get_session
from sqlalchemy import Column, Integer, String, Float


class Alumno(Base):
    """Representa un alumno del sistema SICEI.

    Attributes:
        id (int): Identificador unico, auto-generado por la base de datos.
        nombres (str): Nombres del alumno.
        apellidos (str): Apellidos del alumno.
        matricula (str): Matricula escolar del alumno.
        promedio (float): Promedio academico del alumno.
        password (str): Contrasena del alumno para inicio de sesion.
        fotoPerfilUrl (str): URL de la foto de perfil almacenada en S3.
    """

    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(255), nullable=False)
    apellidos = Column(String(255), nullable=False)
    matricula = Column(String(50), nullable=False)
    promedio = Column(Float, nullable=False)
    password = Column(String(255), nullable=False)
    fotoPerfilUrl = Column(String(512), nullable=True)

    def to_dict(self):
        """Convierte el alumno a un diccionario.

        Returns:
            dict: Representacion del alumno en formato diccionario.
        """
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "matricula": self.matricula,
            "promedio": self.promedio,
            "password": self.password,
            "fotoPerfilUrl": self.fotoPerfilUrl,
        }


def get_all():
    """Obtiene todos los alumnos registrados.

    Returns:
        list[dict]: Lista de alumnos en formato diccionario.
    """
    session = get_session()
    try:
        alumnos = session.query(Alumno).all()
        return [alumno.to_dict() for alumno in alumnos]
    finally:
        session.close()


def get_by_id(id):
    """Busca un alumno por su id.

    Args:
        id (int): Identificador del alumno a buscar.

    Returns:
        dict | None: Diccionario del alumno si existe, None en caso contrario.
    """
    session = get_session()
    try:
        alumno = session.get(Alumno, id)
        return alumno.to_dict() if alumno else None
    finally:
        session.close()


def create(data):
    """Crea un nuevo alumno y lo guarda en la base de datos.

    Args:
        data (dict): Datos del alumno con las llaves nombres, apellidos,
            matricula, promedio y password.

    Returns:
        dict: El alumno creado en formato diccionario, incluyendo el id
            generado por la base de datos.
    """
    session = get_session()
    try:
        alumno = Alumno(
            nombres=data["nombres"],
            apellidos=data["apellidos"],
            matricula=data["matricula"],
            promedio=data["promedio"],
            password=data.get("password", ""),
            fotoPerfilUrl=data.get("fotoPerfilUrl"),
        )
        session.add(alumno)
        session.commit()
        session.refresh(alumno)
        return alumno.to_dict()
    finally:
        session.close()


def update(id, data):
    """Actualiza los datos de un alumno existente.

    Args:
        id (int): Identificador del alumno a actualizar.
        data (dict): Nuevos datos del alumno.

    Returns:
        dict | None: Diccionario del alumno actualizado, None si no existe.
    """
    session = get_session()
    try:
        alumno = session.get(Alumno, id)
        if not alumno:
            return None
        alumno.nombres = data.get("nombres", alumno.nombres)
        alumno.apellidos = data.get("apellidos", alumno.apellidos)
        alumno.matricula = data.get("matricula", alumno.matricula)
        alumno.promedio = data.get("promedio", alumno.promedio)
        if "password" in data:
            alumno.password = data["password"]
        if "fotoPerfilUrl" in data:
            alumno.fotoPerfilUrl = data["fotoPerfilUrl"]
        session.commit()
        session.refresh(alumno)
        return alumno.to_dict()
    finally:
        session.close()


def delete(id):
    """Elimina un alumno de la base de datos.

    Args:
        id (int): Identificador del alumno a eliminar.

    Returns:
        bool: True si se elimino, False si no se encontro.
    """
    session = get_session()
    try:
        alumno = session.get(Alumno, id)
        if not alumno:
            return False
        session.delete(alumno)
        session.commit()
        return True
    finally:
        session.close()


def get_by_matricula(matricula):
    """Busca un alumno por su matricula.

    Args:
        matricula (str): Matricula del alumno.

    Returns:
        Alumno | None: Instancia del alumno o None.
    """
    session = get_session()
    try:
        return session.query(Alumno).filter_by(matricula=matricula).first()
    finally:
        session.close()
