"""Servicio para subir archivos a S3.

Utiliza boto3 con las credenciales configuradas en el entorno para subir
archivos a un bucket publico de S3.
"""

import os
import uuid

import boto3
from botocore.config import Config

BUCKET_NAME = os.getenv("S3_BUCKET", "16001212-uady-aws-academy")
FOTOS_PREFIX = "fotos"


def _get_s3_client():
    """Crea y retorna un cliente de S3 configurado.

    Returns:
        boto3.client: Cliente de S3 listo para usar.
    """
    return boto3.client(
        "s3",
        config=Config(signature_version="s3v4"),
    )


def subir_foto(archivo, alumno_id):
    """Sube una foto de perfil a S3 con permisos publicos.

    Args:
        archivo: Objeto FileStorage de Flask con la imagen.
        alumno_id (int): ID del alumno para nombrar el archivo.

    Returns:
        str: URL publica de la imagen subida a S3.
    """
    s3 = _get_s3_client()
    nombre_archivo = f"{FOTOS_PREFIX}/alumno_{alumno_id}_{uuid.uuid4().hex[:8]}.jpg"

    s3.upload_fileobj(
        archivo,
        BUCKET_NAME,
        nombre_archivo,
        ExtraArgs={
            "ACL": "public-read",
            "ContentType": archivo.content_type or "image/jpeg",
        },
    )

    url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{nombre_archivo}"
    return url
