"""Servicio para enviar notificaciones por SNS.

Utiliza boto3 para publicar mensajes en un topic de SNS configurado
por variable de entorno.
"""

import json
import os

import boto3

SNS_TOPIC_ARN = os.getenv(
    "SNS_TOPIC_ARN",
    "arn:aws:sns:us-east-1:567627288392:sicei-notificaciones",
)


def _get_sns_client():
    """Crea y retorna un cliente de SNS configurado.

    Returns:
        boto3.client: Cliente de SNS listo para usar.
    """
    return boto3.client("sns", region_name="us-east-1")


def enviar_calificaciones(alumno):
    """Envia las calificaciones del alumno al topic de SNS.

    Args:
        alumno (dict): Diccionario con los datos del alumno. Debe incluir
            nombres, apellidos y promedio.

    Returns:
        str: ID del mensaje publicado en SNS.
    """
    sns = _get_sns_client()
    mensaje = (
        f"Calificaciones del alumno:\n\n"
        f"Nombre: {alumno['nombres']} {alumno['apellidos']}\n"
        f"Matricula: {alumno['matricula']}\n"
        f"Promedio: {alumno['promedio']}"
    )
    asunto = f"Calificaciones - {alumno['nombres']} {alumno['apellidos']}"

    respuesta = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=mensaje,
        Subject=asunto,
    )

    return respuesta["MessageId"]
