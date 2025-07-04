from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId

class UserModel(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "SOCIO"

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}