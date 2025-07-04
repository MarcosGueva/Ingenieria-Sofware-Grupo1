from pydantic import BaseModel
from typing import Optional  # Agregar esta importación
class AhorroCreate(BaseModel):
    socio_id: str
    monto: float
    descripcion: Optional[str] = None
