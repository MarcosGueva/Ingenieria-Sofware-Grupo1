from fastapi import APIRouter, HTTPException
from caja_ahorros_api.services.ingreso_egreso_service import registrar_transaccion, listar_ingresos_egresos
from caja_ahorros_api.schemas.ingreso_egreso_schema import IngresoEgresoCreate, IngresoEgresoOut

router = APIRouter()

@router.post("/registrar", response_model=IngresoEgresoOut)
async def registrar_ingreso_egreso_endpoint(ingreso_egreso: IngresoEgresoCreate):
    """
    Endpoint para registrar un ingreso o egreso.
    """
    transaccion_id = await registrar_transaccion(
        ingreso_egreso.tipo,
        ingreso_egreso.monto,
        ingreso_egreso.descripcion,
        ingreso_egreso.entidad
    )
    if not transaccion_id:
        raise HTTPException(status_code=400, detail="Error al registrar la transacción")
    return {"transaccion_id": transaccion_id}

@router.get("/listar", response_model=list[IngresoEgresoOut])
async def listar_ingresos_egresos_endpoint():
    """
    Endpoint para listar todos los ingresos y egresos.
    """
    ingresos_egresos = await listar_ingresos_egresos()
    return ingresos_egresos
