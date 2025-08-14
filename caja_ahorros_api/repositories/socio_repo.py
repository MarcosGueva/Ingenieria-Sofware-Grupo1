from config.database import db
from caja_ahorros_api.models.socio_model import SocioModel
from bson.objectid import ObjectId

async def registrar_socio(socio: SocioModel):
    """
    Registrar un nuevo socio en la base de datos.
    """
    result = await db.socios.insert_one(socio.dict())
    return str(result.inserted_id)

async def obtener_socio(socio_id: str):
    """
    Obtener un socio por su ID.
    """
    return await db.socios.find_one({"_id": ObjectId(socio_id)})

async def actualizar_socio(socio_id: str, socio_data: dict):
    """
    Actualizar la información de un socio.
    """
    await db.socios.update_one({"_id": ObjectId(socio_id)}, {"$set": socio_data})
    return True

async def eliminar_socio(socio_id: str):
    """
    Eliminar un socio de la base de datos.
    """
    await db.socios.delete_one({"_id": ObjectId(socio_id)})
    return True

async def obtener_todos_los_socios():
    """
    Obtener todos los socios registrados.
    """
    return await db.socios.find().to_list(length=100)
