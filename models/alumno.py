alumnos = []


class Alumno:
    """Representa un alumno del sistema SICEI.

    Attributes:
        id (int): Identificador unico del alumno.
        nombres (str): Nombres del alumno.
        apellidos (str): Apellidos del alumno.
        matricula (str): Matricula escolar del alumno.
        promedio (float): Promedio academico del alumno.
    """

    def __init__(self, id, nombres, apellidos, matricula, promedio):
        """Inicializa una nueva instancia de Alumno.

        Args:
            id (int): Identificador unico.
            nombres (str): Nombres del alumno.
            apellidos (str): Apellidos del alumno.
            matricula (str): Matricula escolar.
            promedio (float): Promedio academico.
        """
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.matricula = matricula
        self.promedio = promedio

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
        }


def get_all():
    """Obtiene todos los alumnos registrados.

    Returns:
        list[dict]: Lista de alumnos en formato diccionario.
    """
    return [alumno.to_dict() for alumno in alumnos]


def get_by_id(id):
    """Busca un alumno por su id.

    Args:
        id (int): Identificador del alumno a buscar.

    Returns:
        dict | None: Diccionario del alumno si existe, None en caso contrario.
    """
    for alumno in alumnos:
        if alumno.id == id:
            return alumno.to_dict()
    return None


def create(data):
    """Crea un nuevo alumno y lo agrega al array en memoria.

    Args:
        data (dict): Datos del alumno con las llaves id, nombres, apellidos,
            matricula y promedio.

    Returns:
        dict: El alumno creado en formato diccionario.
    """
    alumno = Alumno(
        id=data["id"],
        nombres=data["nombres"],
        apellidos=data["apellidos"],
        matricula=data["matricula"],
        promedio=data["promedio"],
    )
    alumnos.append(alumno)
    return alumno.to_dict()


def update(id, data):
    """Actualiza los datos de un alumno existente.

    Args:
        id (int): Identificador del alumno a actualizar.
        data (dict): Nuevos datos del alumno.

    Returns:
        dict | None: Diccionario del alumno actualizado, None si no existe.
    """
    for alumno in alumnos:
        if alumno.id == id:
            alumno.nombres = data["nombres"]
            alumno.apellidos = data["apellidos"]
            alumno.matricula = data["matricula"]
            alumno.promedio = data["promedio"]
            return alumno.to_dict()
    return None


def delete(id):
    """Elimina un alumno del array en memoria.

    Args:
        id (int): Identificador del alumno a eliminar.

    Returns:
        bool: True si se elimino, False si no se encontro.
    """
    for i, alumno in enumerate(alumnos):
        if alumno.id == id:
            del alumnos[i]
            return True
    return False
