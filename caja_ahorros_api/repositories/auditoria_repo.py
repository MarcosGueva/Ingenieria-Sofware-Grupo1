from caja_ahorros_api.config.database import db
from caja_ahorros_api.models.auditoria_model import AuditoriaModel
from bson.objectid import ObjectId

async def registrar_evento_auditoria(auditoria: AuditoriaModel):
    """
    Registrar un evento de auditoría en la base de datos.
    """
    result = await db.auditorias.insert_one(auditoria.dict())
    return str(result.inserted_id)

async def obtener_eventos_auditoria():
    """
    Obtener todos los eventos de auditoría.
    """
    return await db.auditorias.find().to_list(length=100)
