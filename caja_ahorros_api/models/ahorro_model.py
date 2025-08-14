from datetime import datetime
from typing import Optional, Literal

from bson import ObjectId
from pydantic import BaseModel, validator


class AhorroModel(BaseModel):
    socio_id: str                                # Referencia al socio (string de ObjectId)
    monto: float                                 # Monto del depósito o retiro
    tipo: Literal["deposito", "retiro"]          # restringido a 2 valores
    descripcion: Optional[str] = None            # Descripción adicional
    created_at: datetime = datetime.utcnow()     # útil para ordenar historiales

    @validator("monto")
    def monto_positivo(cls, v):
        if v <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        return v

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
