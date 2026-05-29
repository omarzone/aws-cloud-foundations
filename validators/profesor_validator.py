def validar_profesor(data):
    """Valida los datos de un profesor.

    Verifica que todos los campos requeridos esten presentes, que los tipos
    de dato sean correctos y que los valores cumplan con las reglas de negocio.

    Args:
        data (dict): Diccionario con los datos del profesor.

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

    if "numeroEmpleado" not in data or not isinstance(
        data["numeroEmpleado"], int
    ):
        errores.append(
            "El campo 'numeroEmpleado' es requerido y debe ser un numero entero"
        )
    elif data["numeroEmpleado"] < 0:
        errores.append(
            "El campo 'numeroEmpleado' no puede ser negativo"
        )

    if "horasClase" not in data or not isinstance(data["horasClase"], int):
        errores.append(
            "El campo 'horasClase' es requerido y debe ser un numero entero"
        )
    elif data["horasClase"] < 0:
        errores.append("El campo 'horasClase' no puede ser negativo")

    return errores if errores else None
