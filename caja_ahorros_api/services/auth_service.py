# caja_ahorros_api/services/auth_service.py

from fastapi import HTTPException, status
from passlib.context import CryptContext
from pymongo.errors import ServerSelectionTimeoutError, DuplicateKeyError

from caja_ahorros_api.config.database import db
from caja_ahorros_api.utils.jwt_utils import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Genera el hash seguro de la contraseña."""
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    """Verifica que la contraseña en texto plano coincida con el hash almacenado."""
    return pwd_context.verify(plain, hashed)


async def ensure_indexes():
    try:
        await db.users.create_index("email", unique=True)
    except ServerSelectionTimeoutError:
        print("[WARN] No se pudo conectar a MongoDB para crear índices. Verifica MONGO_URI o la red.")
    except DuplicateKeyError:
        # Esto es muy raro en email, pero por si acaso:
        print("[WARN] No se pudo crear índice único en email: hay duplicados. Limpia datos.")

    try:
        await db.users.create_index("username", unique=True)
    except DuplicateKeyError:
        print("[WARN] No se pudo crear índice único en username: hay duplicados. La app arrancará sin esa restricción hasta corregir los datos.")
    except ServerSelectionTimeoutError:
        pass

async def register_user(user_data):
    """
    Registra un nuevo usuario.
    Espera un modelo Pydantic con: username, email, password.
    Devuelve: { id, username, email, role }
    """
    # Normalizar entradas
    username = (user_data.username or "").strip()
    email = (user_data.email or "").strip().lower()
    password = user_data.password

    if not username or not email or not password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Faltan campos obligatorios")

    # Comprobaciones previas para mensajes más amigables
    existing_email = await db.users.find_one({"email": email}, {"_id": 1})
    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya está registrado")

    existing_username = await db.users.find_one({"username": username}, {"_id": 1})
    if existing_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre de usuario ya está en uso")

    # Documento a insertar
    user_doc = {
        "username": username,
        "email": email,
        "password": hash_password(password),
        "role": "SOCIO",
    }

    try:
        result = await db.users.insert_one(user_doc)
    except DuplicateKeyError as e:
        # Respaldo por si hay condiciones de carrera entre find_one e insert_one
        msg = "El email ya está registrado"
        # Intento de distinguir por campo, si el driver lo expone (no siempre):
        # Puedes volver a consultar para un mensaje más preciso
        if await db.users.find_one({"username": username}, {"_id": 1}):
            msg = "El nombre de usuario ya está en uso"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)

    # Respuesta pública (sin password)
    return {
        "id": str(result.inserted_id),
        "username": user_doc["username"],
        "email": user_doc["email"],
        "role": user_doc["role"],
    }


async def authenticate_user(email: str, password: str):
    """
    Autentica por email/contraseña.
    Devuelve: { access_token, token_type }
    """
    email_n = (email or "").strip().lower()

    # Traer sólo lo necesario
    user = await db.users.find_one(
        {"email": email_n},
        {"_id": 1, "email": 1, "password": 1, "role": 1}
    )
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token({"sub": user["email"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}
