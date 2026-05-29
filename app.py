from flask import Flask, request, jsonify

from models import alumno
from validators import alumno_validator

app = Flask(__name__)


@app.route("/alumnos", methods=["GET"])
def get_alumnos():
    """Obtiene la lista de todos los alumnos.

    Returns:
        Response: Lista de alumnos en formato JSON con codigo 200.
    """
    return alumno.get_all(), 200


@app.route("/alumnos", methods=["POST"])
def post_alumno():
    """Crea un nuevo alumno.

    Recibe los datos del alumno en formato JSON, los valida y si son
    correctos crea el registro en memoria.

    Returns:
        Response: Alumno creado con codigo 201, o errores de validacion
            con codigo 400.
    """
    data = request.get_json()

    errores = alumno_validator.validar_alumno(data)
    if errores:
        return jsonify({"errores": errores}), 400

    return alumno.create(data), 201


@app.route("/alumnos/<int:id>", methods=["GET"])
def get_alumno(id):
    """Obtiene un alumno por su id.

    Args:
        id (int): Identificador del alumno.

    Returns:
        Response: Alumno encontrado con codigo 200, o error 404 si no existe.
    """
    resultado = alumno.get_by_id(id)
    if resultado is None:
        return jsonify({"error": "Alumno no encontrado"}), 404
    return resultado, 200


@app.route("/alumnos/<int:id>", methods=["PUT"])
def put_alumno(id):
    """Actualiza un alumno existente.

    Args:
        id (int): Identificador del alumno a actualizar.

    Returns:
        Response: Alumno actualizado con codigo 200, error 404 si no existe,
            o errores de validacion con codigo 400.
    """
    data = request.get_json()

    errores = alumno_validator.validar_alumno(data)
    if errores:
        return jsonify({"errores": errores}), 400

    resultado = alumno.update(id, data)
    if resultado is None:
        return jsonify({"error": "Alumno no encontrado"}), 404
    return resultado, 200


@app.route("/alumnos/<int:id>", methods=["DELETE"])
def delete_alumno(id):
    """Elimina un alumno por su id.

    Args:
        id (int): Identificador del alumno a eliminar.

    Returns:
        Response: Codigo 200 si se elimino, o error 404 si no existe.
    """
    eliminado = alumno.delete(id)
    if not eliminado:
        return jsonify({"error": "Alumno no encontrado"}), 404
    return jsonify({"mensaje": "Alumno eliminado"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
