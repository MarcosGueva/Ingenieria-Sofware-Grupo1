from fastapi import APIRouter, HTTPException
from schemas.user_schema import UserCreate, UserLogin, UserOut
from services.auth_service import register_user, authenticate_user

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    new_user = await register_user(user)
    if not new_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    return new_user

@router.post("/login")
async def login(user: UserLogin):
    token = await authenticate_user(user.email, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return token