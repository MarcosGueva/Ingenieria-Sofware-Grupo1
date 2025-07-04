from repositories.socio_repo import registrar_socio, obtener_socio, actualizar_socio, eliminar_socio, obtener_todos_los_socios
from models.socio_model import SocioModel
from fastapi import HTTPException

async def crear_socio(socio_data: SocioModel):
    """
    Registrar un nuevo socio.
    """
    return await registrar_socio(socio_data)

async def obtener_socio_por_id(socio_id: str):
    """
    Obtener los detalles de un socio por su ID.
    """
    socio = await obtener_socio(socio_id)
    if not socio:
        raise HTTPException(status_code=404, detail="Socio no encontrado")
    return socio

async def modificar_socio(socio_id: str, socio_data: dict):
    """
    Actualizar la información de un socio.
    """
    return await actualizar_socio(socio_id, socio_data)

async def eliminar_socio_por_id(socio_id: str):
    """
    Eliminar un socio.
    """
    return await eliminar_socio(socio_id)

async def listar_socios():
    """
    Listar todos los socios.
    """
    return await obtener_todos_los_socios()
