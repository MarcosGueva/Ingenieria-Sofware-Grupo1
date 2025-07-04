from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from openpyxl import Workbook
from io import BytesIO
from config.database import db
from datetime import datetime

def generar_libro_diario():
    """
    Genera un reporte en PDF del libro diario (todas las transacciones).
    """
    response = BytesIO()
    c = canvas.Canvas(response, pagesize=letter)
    c.drawString(100, 800, "Libro Diario - Caja de Ahorros")
    c.drawString(100, 780, f"Fecha: {datetime.now().strftime('%Y-%m-%d')}")
    
    transacciones = db.ahorros.find()  # Asumiendo que 'ahorros' tiene los movimientos de todos los tipos
    y_position = 750
    for trans in transacciones:
        c.drawString(100, y_position, f"ID: {trans['_id']} - Monto: {trans['monto']} - Tipo: {trans['tipo']}")
        y_position -= 20
    
    c.showPage()
    c.save()
    response.seek(0)
    return response

def generar_historial_ahorros(socio_id: str):
    """
    Genera un reporte en Excel del historial de ahorros de un socio.
    """
    wb = Workbook()
    ws = wb.active
    ws.append(["Fecha", "Monto", "Tipo", "Descripción"])
    
    historico = db.ahorros.find({"socio_id": socio_id})
    
    for trans in historico:
        ws.append([trans['fecha'], trans['monto'], trans['tipo'], trans.get('descripcion', '')])
    
    response = BytesIO()
    wb.save(response)
    response.seek(0)
    return response
