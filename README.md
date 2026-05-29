# SICEI REST API

**Autor**: Omar Jesus Cauich Pasos  
**Materia**: AWS Cloud Foundations

API REST para la gestion de alumnos y profesores del sistema SICEI.

## Requisitos

- Python 3.8 o superior
- Flask 3.1.1
- SQLAlchemy 2.0
- boto3 (AWS SDK)
- PyMySQL

## Instalacion

```bash
pip install -r requirements.txt
```

## Ejecucion

```bash
python app.py
```

El servidor se ejecuta en `http://localhost:8080`.

## Endpoints

### Alumnos

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/alumnos` | Obtiene todos los alumnos |
| GET | `/alumnos/{id}` | Obtiene un alumno por id |
| POST | `/alumnos` | Crea un nuevo alumno |
| PUT | `/alumnos/{id}` | Actualiza un alumno existente |
| DELETE | `/alumnos/{id}` | Elimina un alumno |

### Formato JSON para Alumno

```json
{
    "id": 123,
    "nombres": "Eduardo",
    "apellidos": "Rodriguez",
    "matricula": "A123456",
    "promedio": 9.5
}
```

### Profesores

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/profesores` | Obtiene todos los profesores |
| GET | `/profesores/{id}` | Obtiene un profesor por id |
| POST | `/profesores` | Crea un nuevo profesor |
| PUT | `/profesores/{id}` | Actualiza un profesor existente |
| DELETE | `/profesores/{id}` | Elimina un profesor |

### Formato JSON para Profesor

```json
{
    "id": 456,
    "numeroEmpleado": 789,
    "nombres": "Juan",
    "apellidos": "Perez",
    "horasClase": 20
}
```
