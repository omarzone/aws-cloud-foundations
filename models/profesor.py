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
