from pydantic import BaseModel
from typing import Optional

class IngresoEgresoCreate(BaseModel):
    tipo: str  # Puede ser 'ingreso' o 'egreso'
    monto: float
    descripcion: Optional[str] = None

class IngresoEgresoOut(BaseModel):
    id: str
    tipo: str
    monto: float
    descripcion: Optional[str] = None
    fecha: str  # O cualquier formato que necesites
