from fastapi import APIRouter, HTTPException
from services.auditoria_service import obtener_eventos_auditoria

router = APIRouter()

@router.get("/auditoria", response_model=list[dict])
async def consultar_auditoria():
    """
    Endpoint para consultar los eventos de auditoría registrados.
    """
    eventos = await obtener_eventos_auditoria()
    if not eventos:
        raise HTTPException(status_code=404, detail="No se encontraron eventos de auditoría")
    return eventos
