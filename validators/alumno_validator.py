def validar_alumno(data):
    """Valida los datos de un alumno.

    Verifica que todos los campos requeridos esten presentes, que los tipos
    de dato sean correctos y que los valores cumplan con las reglas de negocio.

    Args:
        data (dict): Diccionario con los datos del alumno.

    Returns:
        list[str] | None: Lista de mensajes de error si hay errores de
            validacion, o None si los datos son validos.
    """
    errores = []

    if "nombres" not in data or data["nombres"] is None or data["nombres"] == "":
        errores.append(
            "El campo 'nombres' es requerido y no puede estar vacio"
        )

    if "apellidos" not in data or data["apellidos"] is None:
        errores.append("El campo 'apellidos' es requerido y no puede ser nulo")

    if (
        "matricula" not in data
        or data["matricula"] is None
        or data["matricula"] == ""
        or not isinstance(data["matricula"], str)
    ):
        errores.append(
            "El campo 'matricula' es requerido y debe ser una cadena de texto"
        )

    if "promedio" not in data or not isinstance(data["promedio"], (int, float)):
        errores.append("El campo 'promedio' es requerido y debe ser un numero")
    elif data["promedio"] < 0:
        errores.append("El campo 'promedio' no puede ser negativo")

    if (
        "password" not in data
        or data["password"] is None
        or data["password"] == ""
    ):
        errores.append(
            "El campo 'password' es requerido y no puede estar vacio"
        )

    return errores if errores else None
