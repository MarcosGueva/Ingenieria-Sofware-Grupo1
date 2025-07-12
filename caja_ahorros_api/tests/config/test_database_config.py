
import pytest
from config import database
from motor.motor_asyncio import AsyncIOMotorDatabase

@pytest.mark.asyncio
async def test_get_database_returns_mock_db(mongo_client, monkeypatch):
    """
    Verifica que get_database() devuelva un AsyncIOMotorDatabase
    usando nuestro mongo_client simulado.
    """
    # Parcheamos el client real para que devuelva mongo_client
    monkeypatch.setattr(
        database,
        "AsyncIOMotorClient",
        lambda *args, **kwargs: mongo_client
    )

    db = database.get_database()
    assert isinstance(db, AsyncIOMotorDatabase)
