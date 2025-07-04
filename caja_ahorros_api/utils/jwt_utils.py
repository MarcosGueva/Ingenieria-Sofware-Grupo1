from jose import JWTError, jwt
from datetime import datetime, timedelta
import os
from fastapi import HTTPException, status, Depends
from typing import Optional
from fastapi.security import OAuth2PasswordBearer

# Cargar configuración desde variables de entorno
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "clave_super_secreta")  # Clave secreta de JWT
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")  # Algoritmo de cifrado
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Tiempo de expiración del token

# Dependencia de OAuth2 para la autenticación con JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Función para crear un JWT
def create_access_token(data: dict):
    """
    Crea un token JWT con un tiempo de expiración.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Definir tiempo de expiración
    to_encode.update({"exp": expire})  # Añadir expiración
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Crear el token con la clave secreta

# Función para decodificar el token JWT y obtener los datos
def decode_token(token: str):
    """
    Decodifica el token JWT para obtener los datos del usuario.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Decodificar el token
        return payload  # Devolver los datos contenidos en el token
    except JWTError:
        return None  # Si el token no es válido, retornamos None
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o expirado")

# Función para obtener el usuario actual desde el token JWT
def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Extrae el usuario actual del token JWT.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_token(token)  # Decodificar el token
    if payload is None:
        raise credentials_exception  # Si el token es inválido o ha expirado, lanza excepción
    return payload  # Devolver los datos del usuario

# Función para obtener el rol del usuario actual desde el token JWT
def get_current_user_role(current_user: dict = Depends(get_current_user)):
    """
    Extrae el rol del usuario actual.
    """
    return current_user.get("role")  # Obtener el rol del usuario desde el payload del token

# Verificación de roles (para proteger rutas)
def check_roles(allowed_roles: list):
    """
    Verifica que el usuario tenga uno de los roles permitidos.
    """
    def role_checker(current_user_role: str = Depends(get_current_user_role)):
        if current_user_role not in allowed_roles:  # Si el rol no está en los roles permitidos
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Acceso denegado. Se requieren roles: {allowed_roles}"
            )
        return current_user_role
    return role_checker
