# caja_ahorros_api/repositories/ahorro_repo.py

from datetime import datetime
from typing import List, Dict, Any

from caja_ahorros_api.config.database import db
from caja_ahorros_api.models.ahorro_model import AhorroModel


async def registrar_ahorro(ahorro: AhorroModel) -> str:
    """
    Registrar un depósito o retiro en la base de datos.
    """
    doc = ahorro.dict()
    # Asegurar timestamp (por si el modelo no lo trae)
    doc.setdefault("created_at", datetime.utcnow())

    result = await db.ahorros.insert_one(doc)
    return str(result.inserted_id)


async def obtener_historico_ahorros(socio_id: str) -> List[Dict[str, Any]]:
    """
    Obtener los movimientos históricos de ahorro de un socio,
    ordenados del más antiguo al más reciente.
    """
    cursor = (
        db.ahorros
        .find({"socio_id": socio_id})
        .sort("created_at", 1)
    )
    return await cursor.to_list(length=None)
