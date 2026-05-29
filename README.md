# SICEI REST API

**Autor**: Omar Jesus Cauich Pasos  
**Materia**: AWS Cloud Foundations

API REST para la gestion de alumnos y profesores del sistema SICEI.  
Usa Flask con SQLAlchemy y corre sobre infraestructura de AWS (EC2, RDS, S3, SNS y DynamoDB).

## Requisitos

- Python 3.8 o superior
- MySQL (si se usa RDS) o SQLite (para pruebas locales)

## Instalacion

```bash
pip install -r requirements.txt
```

## Configuracion

Copiar `.env.example` a `.env` y ajustar los valores. En local usa SQLite por defecto, si quieres usar RDS cambia la URL.

```bash
cp .env.example .env
```

Variables:

- `DATABASE_URL` — conexion a la base de datos
- `S3_BUCKET` — bucket de S3 para las fotos de perfil
- `SNS_TOPIC_ARN` — topic de SNS para enviar correos
- `DYNAMODB_TABLE` — tabla de DynamoDB para las sesiones
- `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN` — credenciales de AWS

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
| POST | `/alumnos/{id}/fotoPerfil` | Sube una foto de perfil a S3 |
| POST | `/alumnos/{id}/email` | Envia calificaciones por correo (SNS) |
| POST | `/alumnos/{id}/session/login` | Inicia sesion y devuelve un sessionString |
| POST | `/alumnos/{id}/session/verify` | Verifica si una sesion esta activa |
| POST | `/alumnos/{id}/session/logout` | Cierra la sesion |

### Alumno (JSON)

```json
{
    "nombres": "Eduardo",
    "apellidos": "Rodriguez",
    "matricula": "A123456",
    "promedio": 9.5,
    "password": "miClave123",
    "fotoPerfilUrl": "https://bucket.s3.amazonaws.com/fotos/alumno_1_abc.jpg"
}
```

El `id` lo genera la base de datos automaticamente, no se manda en el POST.

### Profesores

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/profesores` | Obtiene todos los profesores |
| GET | `/profesores/{id}` | Obtiene un profesor por id |
| POST | `/profesores` | Crea un nuevo profesor |
| PUT | `/profesores/{id}` | Actualiza un profesor existente |
| DELETE | `/profesores/{id}` | Elimina un profesor |

### Profesor (JSON)

```json
{
    "numeroEmpleado": 789,
    "nombres": "Juan",
    "apellidos": "Perez",
    "horasClase": 20
}
```

El `id` tambien lo genera la base de datos.
