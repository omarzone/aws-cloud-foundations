"""Servicio para manejar sesiones en DynamoDB.

Gestiona la tabla sesiones-alumnos para login, verificacion y cierre de
sesiones de los alumnos.
"""

import os
import secrets
import time
import uuid

import boto3

TABLE_NAME = "sesiones-alumnos"


def _get_dynamo_client():
    """Crea y retorna un cliente de DynamoDB configurado.

    Returns:
        boto3.client: Cliente de DynamoDB listo para usar.
    """
    return boto3.client("dynamodb", region_name="us-east-1")


def _get_dynamo_resource():
    """Crea y retorna un recurso de DynamoDB para operaciones de alto nivel.

    Returns:
        boto3.resource: Recurso de DynamoDB.
    """
    return boto3.resource("dynamodb", region_name="us-east-1")


def crear_sesion(alumno_id):
    """Crea una nueva sesion activa para un alumno.

    Args:
        alumno_id (int): ID del alumno que inicia sesion.

    Returns:
        str: sessionString de 128 caracteres generado automaticamente.
    """
    session_id = str(uuid.uuid4())
    session_string = secrets.token_hex(64)

    dynamodb = _get_dynamo_resource()
    table = dynamodb.Table(TABLE_NAME)

    item = {
        "id": session_id,
        "fecha": int(time.time()),
        "alumnoId": alumno_id,
        "active": True,
        "sessionString": session_string,
    }
    table.put_item(Item=item)

    return session_string


def verificar_sesion(session_string):
    """Verifica si una sesion esta activa.

    Args:
        session_string (str): String de sesion a verificar.

    Returns:
        bool: True si la sesion existe y esta activa, False en otro caso.
    """
    dynamodb = _get_dynamo_resource()
    table = dynamodb.Table(TABLE_NAME)

    response = table.scan(
        FilterExpression="sessionString = :ss",
        ExpressionAttributeValues={":ss": session_string},
    )

    items = response.get("Items", [])
    if not items:
        return False

    return items[0].get("active", False)


def cerrar_sesion(session_string):
    """Cierra una sesion poniendo active en false.

    Args:
        session_string (str): String de sesion a cerrar.

    Returns:
        bool: True si se cerro correctamente, False si no se encontro.
    """
    dynamodb = _get_dynamo_resource()
    table = dynamodb.Table(TABLE_NAME)

    response = table.scan(
        FilterExpression="sessionString = :ss",
        ExpressionAttributeValues={":ss": session_string},
    )

    items = response.get("Items", [])
    if not items:
        return False

    session_id = items[0]["id"]
    table.update_item(
        Key={"id": session_id},
        UpdateExpression="SET active = :val",
        ExpressionAttributeValues={":val": False},
    )

    return True
