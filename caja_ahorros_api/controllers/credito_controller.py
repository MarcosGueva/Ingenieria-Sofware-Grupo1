from fastapi import APIRouter, HTTPException
from services.credito_service import solicitar_credito, obtener_historial_creditos, aprobar_credito_solicitado
from schemas.credito_schema import CreditoCreate, CreditoOut

router = APIRouter()

@router.post("/solicitar", response_model=CreditoOut)
async def solicitar_credito_endpoint(credito: CreditoCreate):
    """
    Endpoint para solicitar un crédito.
    """
    credito_id = await solicitar_credito(credito)
    if not credito_id:
        raise HTTPException(status_code=400, detail="No se pudo procesar la solicitud")
    return {"credito_id": credito_id}

@router.get("/historial/{socio_id}", response_model=list[CreditoOut])
async def obtener_historial_creditos_endpoint(socio_id: str):
    """
    Endpoint para obtener el historial de créditos de un socio.
    """
    creditos = await obtener_historial_creditos(socio_id)
    if not creditos:
        raise HTTPException(status_code=404, detail="No se encontraron créditos")
    return creditos

@router.post("/aprobar/{credito_id}", response_model=CreditoOut)
async def aprobar_credito_endpoint(credito_id: str):
    """
    Endpoint para aprobar una solicitud de crédito.
    """
    aprobado = await aprobar_credito_solicitado(credito_id)
    if not aprobado:
        raise HTTPException(status_code=400, detail="No se pudo aprobar el crédito")
    return {"message": "Crédito aprobado y tabla de amortización generada"}
