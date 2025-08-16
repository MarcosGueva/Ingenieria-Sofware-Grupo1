from fastapi import APIRouter, HTTPException, status
from ..schemas.user_schema import UserCreate, UserLogin, UserOut, TokenOut
from caja_ahorros_api.services.auth_service import register_user, authenticate_user

router = APIRouter()  # ← SIN prefix aquí

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    new_user = await register_user(user)
    if not new_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    return new_user

@router.post("/login", response_model=TokenOut)
async def login(user: UserLogin):
    token = await authenticate_user(user.email, user.password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return token
