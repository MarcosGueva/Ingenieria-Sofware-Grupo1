
import sys, os

# 1) Determina la ruta absoluta de la carpeta que contiene main.py
tests_dir = os.path.dirname(__file__)              # …/caja_ahorros_api/tests
app_dir   = os.path.abspath(os.path.join(tests_dir, os.pardir))  # …/caja_ahorros_api

# 2) Inserta esa carpeta al inicio de sys.path
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

import pytest
from fastapi.testclient import TestClient
from caja_ahorros_api.main import app           # ahora sí encuentra main.py
from config import database

# Stub mínimo para la base de datos
class DummyMotorClient:
    def __init__(self):
        self._collections = {}
    def __getitem__(self, name):
        return self._collections.setdefault(name, {})

@pytest.fixture(scope="session")
def client():
    return TestClient(app)

@pytest.fixture
def mongo_client(monkeypatch):
    dummy = DummyMotorClient()
    monkeypatch.setattr(
        database,
        "AsyncIOMotorClient",
        lambda *args, **kwargs: dummy
    )
    return dummy