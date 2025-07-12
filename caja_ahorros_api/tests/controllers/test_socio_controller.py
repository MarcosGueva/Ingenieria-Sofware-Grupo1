import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from bson import ObjectId
from controllers.socio_controller import router

# Montamos solo el router de socios para aislar
app_soc = FastAPI()
app_soc.include_router(router, prefix="/socios")
client = TestClient(app_soc)


def test_crear_socio(monkeypatch):
    # Stub async para registrar_socio en service
    async def fake_registrar_socio(socio_data):
        return {"id": "stubid", "nombre": socio_data.nombre, "correo": socio_data.correo}
    monkeypatch.setattr(
        "services.socio_service.registrar_socio",
        fake_registrar_socio
    )

    payload = {"nombre": "Ana", "correo": "a@a.com"}
    resp = client.post("/socios/registrar", json=payload)
    assert resp.status_code in (200, 201)
    data = resp.json()
    # Debe coincidir exactamente con el dict retornado por el stub
    assert data == {"id": "stubid", "nombre": "Ana", "correo": "a@a.com"}


def test_listar_socios(monkeypatch):
    # Stub async para listar_socios en service
    async def fake_listar_socios():
        return [{"id": "stub1", "nombre": "X", "correo": "x@y.com"}]
    monkeypatch.setattr(
        "services.socio_service.listar_socios",
        fake_listar_socios
    )

    resp = client.get("/socios/listar")
    assert resp.status_code == 200
    arr = resp.json()
    # Debe devolver la lista exacta del stub
    assert arr == [{"id": "stub1", "nombre": "X", "correo": "x@y.com"}]


def test_obtener_socio(monkeypatch):
    test_id = str(ObjectId())
    # Stub async para obtener_socio_por_id en controller
    async def fake_obtener_socio_por_id(sid):
        return {"id": sid, "nombre": "Ana", "correo": "a@a.com"}
    monkeypatch.setattr(
        "controllers.socio_controller.obtener_socio_por_id",
        fake_obtener_socio_por_id
    )

    resp = client.get(f"/socios/{test_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data == {"id": test_id, "nombre": "Ana", "correo": "a@a.com"}


def test_eliminar_socio(monkeypatch):
    test_id = str(ObjectId())
    # Stub async para eliminar_socio_por_id en controller
    async def fake_eliminar_socio_por_id(sid):
        return True
    monkeypatch.setattr(
        "controllers.socio_controller.eliminar_socio_por_id",
        fake_eliminar_socio_por_id
    )

    resp = client.delete(f"/socios/{test_id}")
    assert resp.status_code == 200
    # Debe devolver el mensaje esperado
    assert resp.json() == {"message": "Socio eliminado exitosamente"}
