from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from openpyxl import Workbook
from io import BytesIO
from caja_ahorros_api.config.database import db
from datetime import datetime

def generar_reporte_ingresos_egresos_pdf():
    """
    Genera un reporte en PDF con todos los ingresos y egresos registrados.
    """
    response = BytesIO()
    c = canvas.Canvas(response, pagesize=letter)
    c.drawString(100, 800, "Reporte de Ingresos y Egresos - Caja de Ahorros")
    c.drawString(100, 780, f"Fecha: {datetime.now().strftime('%Y-%m-%d')}")
    
    # Obtener todos los ingresos y egresos
    transacciones = db.ingresos_egresos.find()
    y_position = 750
    for trans in transacciones:
        c.drawString(100, y_position, f"ID: {trans['_id']} - Monto: {trans['monto']} - Tipo: {trans['tipo']} - Entidad: {trans['entidad']}")
        y_position -= 20
    
    c.showPage()
    c.save()
    response.seek(0)
    return response

def generar_reporte_ingresos_egresos_excel():
    """
    Genera un reporte en Excel con todos los ingresos y egresos registrados.
    """
    wb = Workbook()
    ws = wb.active
    ws.append(["ID", "Monto", "Tipo", "Entidad", "Fecha"])
    
    # Obtener todos los ingresos y egresos
    transacciones = db.ingresos_egresos.find()
    
    for trans in transacciones:
        ws.append([str(trans['_id']), trans['monto'], trans['tipo'], trans['entidad'], trans['fecha']])
    
    response = BytesIO()
    wb.save(response)
    response.seek(0)
    return response
