from caja_ahorros_api.schemas.ahorro_schema import AhorroModel

from pydantic import BaseModel
from typing import Optional  # Agregar esta importación
class AhorroCreate(BaseModel):
    socio_id: str
    monto: float
    descripcion: Optional[str] = None
