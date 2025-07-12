import pytest
from pydantic import ValidationError
from models.credito_model import CreditoModel, AmortizacionModel


def test_credito_model_valid():
    """
    CreditoModel debe aceptar parámetros correctos.
    """
    credito = CreditoModel(
        socio_id="507f1f77bcf86cd799439011",
        monto=1500.0,
        plazo_meses=12,
        tasa_interes=0.08
    )
    assert credito.socio_id == "507f1f77bcf86cd799439011"
    assert credito.monto == 1500.0
    assert credito.plazo_meses == 12
    assert credito.tasa_interes == 0.08

# Para AmortizacionModel, provee los campos obligatorios según error:

def test_amortizacion_model_valid():
    """
    AmortizacionModel debe validar los campos obligatorios.
    """
    # Incluimos los campos requeridos: credito_id, cuota, monto_cuota
    amort = AmortizacionModel(
        credito_id="507f1f77bcf86cd799439011",
        cuota=100.0,
        monto_cuota=100.0
    )
    assert amort.credito_id == "507f1f77bcf86cd799439011"
    assert amort.cuota == 100.0
    assert amort.monto_cuota == 100.0