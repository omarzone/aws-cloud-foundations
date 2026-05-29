from flask import Flask

from models import alumno

app = Flask(__name__)


@app.route("/alumnos", methods=["GET"])
def get_alumnos():
    """Obtiene la lista de todos los alumnos.

    Returns:
        Response: Lista de alumnos en formato JSON con codigo 200.
    """
    return alumno.get_all(), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
