from config.database import db
from models.ingreso_egreso_model import IngresoEgresoModel
from bson.objectid import ObjectId

async def registrar_ingreso_egreso(transaccion: IngresoEgresoModel):
    """
    Registrar un ingreso o egreso en la base de datos.
    """
    result = await db.ingresos_egresos.insert_one(transaccion.dict())
    return str(result.inserted_id)

async def obtener_ingresos_egresos():
    """
    Obtener todos los ingresos y egresos registrados.
    """
    return await db.ingresos_egresos.find().to_list(length=100)
