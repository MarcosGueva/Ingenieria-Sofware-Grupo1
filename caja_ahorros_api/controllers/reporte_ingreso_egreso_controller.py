from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from services.reporte_ingreso_egreso_service import generar_reporte_ingresos_egresos_pdf, generar_reporte_ingresos_egresos_excel

router = APIRouter()

@router.get("/reporte-pdf", response_class=StreamingResponse)
async def obtener_reporte_pdf():
    """
    Endpoint para obtener el reporte de ingresos y egresos en formato PDF.
    """
    pdf_file = generar_reporte_ingresos_egresos_pdf()
    return StreamingResponse(pdf_file, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=reporte_ingresos_egresos.pdf"})

@router.get("/reporte-excel", response_class=StreamingResponse)
async def obtener_reporte_excel():
    """
    Endpoint para obtener el reporte de ingresos y egresos en formato Excel.
    """
    excel_file = generar_reporte_ingresos_egresos_excel()
    return StreamingResponse(excel_file, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                             headers={"Content-Disposition": "attachment; filename=reporte_ingresos_egresos.xlsx"})