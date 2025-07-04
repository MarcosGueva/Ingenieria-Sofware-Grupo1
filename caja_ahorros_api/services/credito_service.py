from repositories.credito_repo import registrar_credito, obtener_credito, aprobar_credito
from models.credito_model import CreditoModel

async def solicitar_credito(credito_data: CreditoModel):
    """
    Solicitar un crédito (registrar en la base de datos).
    """
    # Aquí puedes agregar validaciones (por ejemplo, si el socio tiene historial positivo)
    return await registrar_credito(credito_data)

async def obtener_historial_creditos(socio_id: str):
    """
    Obtener los créditos solicitados por un socio.
    """
    return await obtener_credito(socio_id)

async def aprobar_credito_solicitado(credito_id: str):
    """
    Aprobar una solicitud de crédito y generar la tabla de amortización.
    """
    return await aprobar_credito(credito_id)
