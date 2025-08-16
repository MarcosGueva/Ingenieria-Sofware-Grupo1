from pydantic import BaseModel
from typing import Optional

class SocioCreate(BaseModel):
    nombre: str
    correo: str
    telefono: Optional[str] = None  # Esto es un campo opcional
    direccion: Optional[str] = None  # Otro campo opcional

class SocioOut(BaseModel):
    id: str
    nombre: str
    correo: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None

