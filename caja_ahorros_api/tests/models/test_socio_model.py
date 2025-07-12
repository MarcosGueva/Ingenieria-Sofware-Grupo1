import pytest
from pydantic import ValidationError
from models.socio_model import SocioModel


def test_socio_model_valid():
    """
    SocioModel debe validar correctamente los campos obligatorios.
    """
    # Incluye nombre, apellido y email según definición real
    socio = SocioModel(
        nombre="Ana",
        apellido="Perez",
        email="ana@correo.com"
    )
    assert socio.nombre == "Ana"
    assert socio.apellido == "Perez"
    assert socio.email == "ana@correo.com"


def test_socio_model_missing_fields():
    """
    Debe fallar si falta algún campo obligatorio.
    """
    with pytest.raises(ValidationError):
        SocioModel(nombre="Ana")  # faltan apellido y email