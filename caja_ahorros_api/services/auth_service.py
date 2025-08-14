from caja_ahorros_api.config.database import db
from passlib.context import CryptContext
from caja_ahorros_api.utils.jwt_utils import (
    create_access_token,
)
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

async def ensure_indexes():
    """
    Crea índices necesarios (idempotente). Llama una vez al arrancar la app.
    """
    await db.users.create_index("email", unique=True)

async def register_user(user_data):
    # Normalizar email
    email = user_data.email.strip().lower()

    # ¿existe?
    existing = await db.users.find_one({"email": email}, {"_id": 1})
    if existing:
        # Puedes devolver None si tu controller lo maneja;
        # lanzar HTTPException te da mensaje y status claros:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo ya está registrado",
        )

    # Construir documento seguro
    user_doc = user_data.dict()
    user_doc["email"] = email
    user_doc["password"] = hash_password(user_doc["password"])
    user_doc["role"] = user_doc.get("role") or "SOCIO"

    result = await db.users.insert_one(user_doc)

    # Nunca devolver password
    return {
        "id": str(result.inserted_id),
        "name": user_doc.get("name"),
        "email": user_doc["email"],
        "role": user_doc["role"],
    }

async def authenticate_user(email: str, password: str):
    email_n = (email or "").strip().lower()

    # Trae solo lo necesario
    user = await db.users.find_one(
        {"email": email_n},
        {"_id": 1, "email": 1, "password": 1, "role": 1}
    )
    if not user or not verify_password(password, user["password"]):
        # Devuelve None si tu controller lo traduce a 401, o lanza aquí
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token({"sub": user["email"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}
