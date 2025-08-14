from fastapi import HTTPException
from caja_ahorros_api.models.ahorro_model import AhorroModel
from caja_ahorros_api.repositories.ahorro_repo import (
    registrar_ahorro,
    obtener_historico_ahorros,
)
from caja_ahorros_api.models.ahorro_model import AhorroModel  # <- lo usas abajo


async def realizar_deposito(socio_id: str, monto: float, descripcion: str = ""):
    """
    Realizar un depósito en la cuenta de un socio.
    """
    if monto <= 0:
        raise HTTPException(status_code=400, detail="El monto debe ser mayor a cero")

    # Registrar el depósito
    ahorro = AhorroModel(
        socio_id=socio_id,
        monto=monto,
        tipo="deposito",
        descripcion=descripcion,
    )
    await registrar_ahorro(ahorro)
    return {"message": "Depósito realizado correctamente"}


async def realizar_retiro(socio_id: str, monto: float, descripcion: str = ""):
    """
    Realizar un retiro de la cuenta de un socio.
    """
    if monto <= 0:
        raise HTTPException(status_code=400, detail="El monto debe ser mayor a cero")

    # Obtener el histórico de ahorros
    historico = await obtener_historico_ahorros(socio_id)
    saldo_total = sum(
        (mov["monto"] if mov["tipo"] == "deposito" else -mov["monto"])
        for mov in historico
    )

    if saldo_total < monto:
        raise HTTPException(status_code=400, detail="Saldo insuficiente para realizar el retiro")

    # Registrar el retiro
    ahorro = AhorroModel(
        socio_id=socio_id,
        monto=monto,
        tipo="retiro",
        descripcion=descripcion,
    )
    await registrar_ahorro(ahorro)
    return {"message": "Retiro realizado correctamente", "saldo_restante": saldo_total - monto}