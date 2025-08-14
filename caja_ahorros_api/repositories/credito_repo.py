from caja_ahorros_api.config.database import db
from caja_ahorros_api.models.credito_model import CreditoModel, AmortizacionModel
from bson.objectid import ObjectId

async def registrar_credito(credito: CreditoModel):
    """
    Registrar una nueva solicitud de crédito.
    """
    result = await db.creditos.insert_one(credito.dict())
    return str(result.inserted_id)

async def obtener_credito(socio_id: str):
    """
    Obtener los créditos solicitados por un socio.
    """
    return await db.creditos.find({"socio_id": socio_id}).to_list(length=100)

async def aprobar_credito(credito_id: str):
    """
    Aprobar la solicitud de crédito y generar la tabla de amortización.
    """
    credito = await db.creditos.find_one({"_id": ObjectId(credito_id)})
    if credito and credito["estado"] == "pendiente":
        # Actualizar estado del crédito
        await db.creditos.update_one(
            {"_id": ObjectId(credito_id)}, {"$set": {"estado": "aprobado", "aprobado": True}}
        )
        # Crear tabla de amortización
        await generar_amortizacion(credito_id, credito["monto"], credito["tasa_interes"], credito["plazo_meses"])
        return True
    return False

async def generar_amortizacion(credito_id: str, monto: float, tasa_interes: float, plazo_meses: int):
    """
    Generar la tabla de amortización para un crédito aprobado.
    """
    cuota_fija = (monto * (tasa_interes / 100) * (1 + tasa_interes / 100) ** plazo_meses) / ((1 + tasa_interes / 100) ** plazo_meses - 1)
    for mes in range(1, plazo_meses + 1):
        amortizacion = AmortizacionModel(credito_id=credito_id, cuota=mes, monto_cuota=cuota_fija)
        await db.amortizaciones.insert_one(amortizacion.dict())
