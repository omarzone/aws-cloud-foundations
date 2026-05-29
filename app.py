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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
