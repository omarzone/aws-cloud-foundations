# SICEI REST API

**Autor**: Omar Jesus Cauich Pasos  
**Materia**: AWS Cloud Foundations

API REST para la gestion de alumnos y profesores del sistema SICEI.

## Requisitos

- Python 3.8 o superior
- Flask 3.1.1

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
