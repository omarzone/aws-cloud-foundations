profesores = []


class Profesor:
    """Representa un profesor del sistema SICEI.

    Attributes:
        id (int): Identificador unico del profesor.
        numeroEmpleado (int): Numero de empleado del profesor.
        nombres (str): Nombres del profesor.
        apellidos (str): Apellidos del profesor.
        horasClase (int): Horas de clase asignadas al profesor.
    """

    def __init__(self, id, numeroEmpleado, nombres, apellidos, horasClase):
        """Inicializa una nueva instancia de Profesor.

        Args:
            id (int): Identificador unico.
            numeroEmpleado (int): Numero de empleado.
            nombres (str): Nombres del profesor.
            apellidos (str): Apellidos del profesor.
            horasClase (int): Horas de clase asignadas.
        """
        self.id = id
        self.numeroEmpleado = numeroEmpleado
        self.nombres = nombres
        self.apellidos = apellidos
        self.horasClase = horasClase

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
    return [profesor.to_dict() for profesor in profesores]


def get_by_id(id):
    """Busca un profesor por su id.

    Args:
        id (int): Identificador del profesor a buscar.

    Returns:
        dict | None: Diccionario del profesor si existe, None en caso contrario.
    """
    for profesor in profesores:
        if profesor.id == id:
            return profesor.to_dict()
    return None


def create(data):
    """Crea un nuevo profesor y lo agrega al array en memoria.

    Args:
        data (dict): Datos del profesor con las llaves id, numeroEmpleado,
            nombres, apellidos y horasClase.

    Returns:
        dict: El profesor creado en formato diccionario.
    """
    profesor = Profesor(
        id=data["id"],
        numeroEmpleado=data["numeroEmpleado"],
        nombres=data["nombres"],
        apellidos=data["apellidos"],
        horasClase=data["horasClase"],
    )
    profesores.append(profesor)
    return profesor.to_dict()


def update(id, data):
    """Actualiza los datos de un profesor existente.

    Args:
        id (int): Identificador del profesor a actualizar.
        data (dict): Nuevos datos del profesor.

    Returns:
        dict | None: Diccionario del profesor actualizado, None si no existe.
    """
    for profesor in profesores:
        if profesor.id == id:
            profesor.numeroEmpleado = data["numeroEmpleado"]
            profesor.nombres = data["nombres"]
            profesor.apellidos = data["apellidos"]
            profesor.horasClase = data["horasClase"]
            return profesor.to_dict()
    return None


def delete(id):
    """Elimina un profesor del array en memoria.

    Args:
        id (int): Identificador del profesor a eliminar.

    Returns:
        bool: True si se elimino, False si no se encontro.
    """
    for i, profesor in enumerate(profesores):
        if profesor.id == id:
            del profesores[i]
            return True
    return False
