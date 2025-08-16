# caja_ahorros_api/schemas/user_schema.py
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    username: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=6)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)

class UserOut(BaseModel):
    id: str
    username: str
    email: EmailStr
    role: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
