import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from controllers.auth_controller import router

# Montamos solo el router de auth para aislar
app_auth = FastAPI()
app_auth.include_router(router, prefix="/auth")
client = TestClient(app_auth)

def test_register_user(monkeypatch):
    # Stub de la función interna que registra el usuario
    async def fake_register_user(user_data):
        return {"id": "U1", "username": user_data.username, "email": user_data.email, "role": "user"}

    monkeypatch.setattr(
        "controllers.auth_controller.register_user",
        fake_register_user
    )

    payload = {"username": "User1", "email": "u@u.com", "password": "secret"}
    resp = client.post("/auth/register", json=payload)
    # El endpoint devuelve 200 OK
    assert resp.status_code == 200
    assert resp.json() == {
        "id": "U1",
        "username": "User1",
        "email": "u@u.com",
        "role": "user"
    }


def test_login(monkeypatch):
    # Stub de authenticate_user para devolver un dict con hashed_password y role
    async def fake_authenticate_user(email, password):
        return {"id": "U1", "username": "User1", "email": email, "hashed_password": "fakehash", "role": "user"}

    # Parcheamos authenticate_user en el controller
    monkeypatch.setattr(
        "controllers.auth_controller.authenticate_user",
        fake_authenticate_user
    )

    payload = {"email": "u@u.com", "password": "secret"}
    resp = client.post("/auth/login", json=payload)
    assert resp.status_code == 200
    # El controller devuelve directamente el usuario (UserOut)
    assert resp.json() == {"id": "U1", "username": "User1", "email": "u@u.com", "role": "user"}