import pytest
from bson.objectid import ObjectId
from repositories.socio_repo import registrar_socio, obtener_socio

@pytest.mark.asyncio
async def test_registrar_y_obtener_socio(monkeypatch):
    # Stub de colección con insert_one y find_one, asociada a un ObjectId válido
    class CollStub:
        def __init__(self):
            self._data = {}
        async def insert_one(self, doc):
            rid = ObjectId()
            self._data.update(doc)
            return type("R", (), {"inserted_id": rid})
        async def find_one(self, query):
            return {"_id": query["_id"], **self._data}

    # Parcheamos socio_repo.db para que use nuestra colección stub
    import repositories.socio_repo as sr_mod
    stub_coll = CollStub()
    stub_db = type("D", (), {"socios": stub_coll})
    monkeypatch.setattr(sr_mod, "db", stub_db)

    # Creamos un modelo mínimo que tenga dict()
    class FakeSocio:
        def dict(self):
            return {"nombre": "Ana"}

    # Probar registrar_socio
    new_id = await registrar_socio(FakeSocio())
    # Verifica que new_id es una cadena y corresponde al ObjectId generado
    assert isinstance(new_id, str)
    assert str(ObjectId(new_id)) == new_id

    # Probar obtener_socio con el mismo ID
    socio = await obtener_socio(new_id)
    assert socio["nombre"] == "Ana"
