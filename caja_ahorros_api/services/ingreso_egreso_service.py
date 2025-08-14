from caja_ahorros_api.repositories.ingreso_egreso_repo import (
    registrar_ingreso_egreso,
    obtener_ingresos_egresos,
)
from caja_ahorros_api.models.ingreso_egreso_model import IngresoEgresoModel
from fastapi import HTTPException

async def registrar_transaccion(tipo: str, monto: float, descripcion: str, entidad: str):
    """
    Registrar un ingreso o egreso en el sistema.
    """
    if tipo not in ['ingreso', 'egreso']:
        raise HTTPException(status_code=400, detail="El tipo de transacción debe ser 'ingreso' o 'egreso'")
    if monto <= 0:
        raise HTTPException(status_code=400, detail="El monto debe ser mayor a cero")
    
    transaccion = IngresoEgresoModel(tipo=tipo, monto=monto, descripcion=descripcion, entidad=entidad)
    return await registrar_ingreso_egreso(transaccion)

async def listar_ingresos_egresos():
    """
    Obtener todos los ingresos y egresos registrados.
    """
    return await obtener_ingresos_egresos()
