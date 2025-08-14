from fastapi import APIRouter
from caja_ahorros_api.services.ahorro_service import realizar_deposito, realizar_retiro
from caja_ahorros_api.schemas.ahorro_schema import AhorroCreate

router = APIRouter()

@router.post("/depositar")
async def depositar(ahorro: AhorroCreate):
    """Endpoint para realizar un depósito en la cuenta de un socio."""
    return await realizar_deposito(ahorro.socio_id, ahorro.monto, ahorro.descripcion)

@router.post("/retirar")
async def retirar(ahorro: AhorroCreate):
    """Endpoint para realizar un retiro de la cuenta de un socio."""
    return await realizar_retiro(ahorro.socio_id, ahorro.monto, ahorro.descripcion)
