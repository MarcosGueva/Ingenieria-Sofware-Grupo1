from pydantic import BaseModel

class CreditoCreate(BaseModel):
    socio_id: str
    monto: float
    tasa_interes: float
    plazo_meses: int

class CreditoOut(BaseModel):
    socio_id: str
    monto: float
    tasa_interes: float
    plazo_meses: int
    aprobado: bool
    estado: str
