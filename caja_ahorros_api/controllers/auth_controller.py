from fastapi import APIRouter, HTTPException
from ..schemas.user_schema   import UserCreate, UserLogin, UserOut
from caja_ahorros_api.services.auth_service import register_user, authenticate_user
from caja_ahorros_api.utils.jwt_utils import get_current_user, check_roles

router = APIRouter()

@router.post("/register", response_model=UserOut, summary="Registrar un nuevo usuario", description="Este endpoint registra un nuevo usuario en el sistema. Requiere nombre, email y contraseña.")
async def register(user: UserCreate):
    """
    Endpoint para registrar un nuevo usuario.
    """
    new_user = await register_user(user)
    if not new_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    return new_user

@router.post("/login", response_model=UserOut, summary="Iniciar sesión", description="Este endpoint permite a los usuarios iniciar sesión en el sistema y obtener un token JWT para autenticación.")
async def login(user: UserLogin):
    """
    Endpoint para iniciar sesión y obtener un token JWT.
    """
    token = await authenticate_user(user.email, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return token