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
