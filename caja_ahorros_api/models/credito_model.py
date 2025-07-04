from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class CreditoModel(BaseModel):
    socio_id: str  # ID del socio que solicita el crédito
    monto: float   # Monto solicitado
    tasa_interes: float  # Tasa de interés
    plazo_meses: int  # Plazo en meses
    aprobado: bool = False  # Si el crédito ha sido aprobado
    estado: str = "pendiente"  # Estado del crédito (pendiente, aprobado, rechazado)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class AmortizacionModel(BaseModel):
    credito_id: str  # ID del crédito
    cuota: int  # Número de la cuota
    monto_cuota: float  # Monto de la cuota
    fecha_pago: Optional[str] = None  # Fecha de pago (si ha sido pagada)
