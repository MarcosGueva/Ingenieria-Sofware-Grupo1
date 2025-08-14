from config.database import db
from caja_ahorros_api.models.ahorro_model import AhorroModel
from bson.objectid import ObjectId

async def registrar_ahorro(ahorro: AhorroModel):
    """
    Registrar un depósito o retiro en la base de datos.
    """
    result = await db.ahorros.insert_one(ahorro.dict())
    return str(result.inserted_id)

async def obtener_historico_ahorros(socio_id: str):
    """
    Obtener los movimientos históricos de ahorro de un socio.
    """
    return await db.ahorros.find({"socio_id": socio_id}).to_list(length=100)
