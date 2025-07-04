from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from services.reporte_service import generar_libro_diario, generar_historial_ahorros

router = APIRouter()

@router.get("/libro-diario", response_class=StreamingResponse)
async def libro_diario():
    """
    Endpoint para generar el reporte del libro diario (PDF).
    """
    pdf_file = generar_libro_diario()
    return StreamingResponse(pdf_file, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=libro_diario.pdf"})

@router.get("/historial-ahorros/{socio_id}", response_class=StreamingResponse)
async def historial_ahorros(socio_id: str):
    """
    Endpoint para generar el historial de ahorros de un socio (Excel).
    """
    excel_file = generar_historial_ahorros(socio_id)
    return StreamingResponse(excel_file, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                             headers={"Content-Disposition": f"attachment; filename=historial_ahorros_{socio_id}.xlsx"})
