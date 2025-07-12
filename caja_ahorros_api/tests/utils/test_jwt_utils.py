from main import app
from utils.jwt_utils import create_access_token, decode_token
from datetime import timedelta

def test_jwt_roundtrip():
    # Genera un token con la configuración por defecto
    token = create_access_token({"sub": "u1"})
    # Decodifica el token
    payload = decode_token(token)
    assert payload["sub"] == "u1"