from typing import Optional  # Asegúrate de importar Optional
from repositories.auditoria_repo import registrar_evento_auditoria, obtener_eventos_auditoria as obtener_eventos_auditoria_repo  # Asegúrate de que la función obtener_eventos_auditoria esté correctamente referenciada
from caja_ahorros_api.models.auditoria_model import AuditoriaModel
from datetime import datetime

async def registrar_accion_auditoria(accion: str, usuario_id: str, entidad: str, datos: Optional[dict] = None):
    """
    Registrar una acción realizada por un usuario.
    """
    auditoria = AuditoriaModel(
        accion=accion,
        usuario_id=usuario_id,
        entidad=entidad,
        datos=datos,
        fecha=datetime.utcnow()  # La fecha y hora actual
    )
    # Llamamos al repositorio para registrar la acción
    return await registrar_evento_auditoria(auditoria)

async def obtener_eventos_auditoria():
    """
    Obtener los eventos de auditoría registrados.
    """
    # Asegúrate de llamar a la función correcta del repositorio
    return await obtener_eventos_auditoria_repo()
