from pydantic import BaseModel, EmailStr
from bson import ObjectId
from typing import Optional
from datetime import datetime

class SocioModel(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    fecha_registro: datetime = datetime.utcnow()

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
