from pydantic import BaseModel
from bson import ObjectId
from typing import Optional

class AhorroModel(BaseModel):
    socio_id: str  # Referencia al socio
    monto: float   # Monto del depósito o retiro
    tipo: str      # 'deposito' o 'retiro'
    descripcion: Optional[str] = None  # Descripción adicional

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
