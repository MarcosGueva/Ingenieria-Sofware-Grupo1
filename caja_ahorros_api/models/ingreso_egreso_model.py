from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
from datetime import datetime

class IngresoEgresoModel(BaseModel):
    tipo: str  # 'ingreso' o 'egreso'
    monto: float
    descripcion: Optional[str] = None
    fecha: datetime = datetime.utcnow()
    entidad: str  # Entidad que realiza el ingreso o egreso (ej: "Caja de Ahorros", "Socio", etc.)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
