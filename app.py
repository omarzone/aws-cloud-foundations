from flask import Flask, request, jsonify

from config.database import init_db
from models import alumno, profesor
from services import s3_service, sns_service
from validators import alumno_validator, profesor_validator

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    """Maneja rutas no encontradas.

    Args:
        error: El error 404 generado por Flask.

    Returns:
        Response: Mensaje de error en JSON con codigo 404.
    """
    return jsonify({"error": "Ruta no encontrada"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Maneja metodos HTTP no soportados en rutas existentes.

    Args:
        error: El error 405 generado por Flask.

    Returns:
        Response: Mensaje de error en JSON con codigo 405.
    """
    return jsonify({"error": "Metodo no permitido"}), 405


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
    correctos guarda el registro en la base de datos.

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


@app.route("/profesores", methods=["GET"])
def get_profesores():
    """Obtiene la lista de todos los profesores.

    Returns:
        Response: Lista de profesores en formato JSON con codigo 200.
    """
    return profesor.get_all(), 200


@app.route("/profesores", methods=["POST"])
def post_profesor():
    """Crea un nuevo profesor.

    Recibe los datos del profesor en formato JSON, los valida y si son
    correctos guarda el registro en la base de datos.

    Returns:
        Response: Profesor creado con codigo 201, o errores de validacion
            con codigo 400.
    """
    data = request.get_json()

    errores = profesor_validator.validar_profesor(data)
    if errores:
        return jsonify({"errores": errores}), 400

    return profesor.create(data), 201


@app.route("/profesores/<int:id>", methods=["GET"])
def get_profesor(id):
    """Obtiene un profesor por su id.

    Args:
        id (int): Identificador del profesor.

    Returns:
        Response: Profesor encontrado con codigo 200, o error 404 si no existe.
    """
    resultado = profesor.get_by_id(id)
    if resultado is None:
        return jsonify({"error": "Profesor no encontrado"}), 404
    return resultado, 200


@app.route("/profesores/<int:id>", methods=["PUT"])
def put_profesor(id):
    """Actualiza un profesor existente.

    Args:
        id (int): Identificador del profesor a actualizar.

    Returns:
        Response: Profesor actualizado con codigo 200, error 404 si no existe,
            o errores de validacion con codigo 400.
    """
    data = request.get_json()

    errores = profesor_validator.validar_profesor(data)
    if errores:
        return jsonify({"errores": errores}), 400

    resultado = profesor.update(id, data)
    if resultado is None:
        return jsonify({"error": "Profesor no encontrado"}), 404
    return resultado, 200


@app.route("/profesores/<int:id>", methods=["DELETE"])
def delete_profesor(id):
    """Elimina un profesor por su id.

    Args:
        id (int): Identificador del profesor a eliminar.

    Returns:
        Response: Codigo 200 si se elimino, o error 404 si no existe.
    """
    eliminado = profesor.delete(id)
    if not eliminado:
        return jsonify({"error": "Profesor no encontrado"}), 404
    return jsonify({"mensaje": "Profesor eliminado"}), 200


@app.route("/alumnos/<int:id>/fotoPerfil", methods=["POST"])
def post_foto_perfil(id):
    """Sube una foto de perfil para un alumno.

    Recibe una imagen en formato multipart/form-data, la sube a S3 y
    guarda la URL en el perfil del alumno.

    Args:
        id (int): Identificador del alumno.

    Returns:
        Response: URL de la foto con codigo 200, o error 404 si el
            alumno no existe.
    """
    if "foto" not in request.files:
        return jsonify({"error": "No se envio ninguna foto"}), 400

    alumno_existente = alumno.get_by_id(id)
    if alumno_existente is None:
        return jsonify({"error": "Alumno no encontrado"}), 404

    foto = request.files["foto"]
    url = s3_service.subir_foto(foto, id)
    alumno.update(id, {"fotoPerfilUrl": url})

    return jsonify({"fotoPerfilUrl": url}), 200


@app.route("/alumnos/<int:id>/email", methods=["POST"])
def post_email(id):
    """Envia las calificaciones del alumno por correo usando SNS.

    Publica un mensaje en el topic de SNS con los datos y calificaciones
    del alumno.

    Args:
        id (int): Identificador del alumno.

    Returns:
        Response: Mensaje de confirmacion con codigo 200, o error 404
            si el alumno no existe.
    """
    alumno_data = alumno.get_by_id(id)
    if alumno_data is None:
        return jsonify({"error": "Alumno no encontrado"}), 404

    sns_service.enviar_calificaciones(alumno_data)
    return jsonify({"mensaje": "Calificaciones enviadas"}), 200


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8080, debug=True)
