from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
from datetime import datetime

class AuditoriaModel(BaseModel):
    accion: str  # Acción realizada (ej: "crear", "editar", "eliminar")
    usuario_id: str  # ID del usuario que realizó la acción
    entidad: str  # La entidad sobre la cual se realizó la acción (ej: "socio", "ahorro")
    datos: Optional[dict] = None  # Datos modificados o creados, si corresponde
    fecha: datetime  # Fecha y hora de la acción

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
