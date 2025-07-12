
import pytest
from pydantic import ValidationError
from schemas.socio_schema import SocioCreate, SocioOut

def test_socio_create_valid():
    # Cambiamos `email` por `correo`
    s = SocioCreate(nombre="Carlos", correo="c@c.com")
    assert s.nombre == "Carlos"
    assert s.correo == "c@c.com"

def test_socio_create_missing_field():
    # Falta el nombre
    with pytest.raises(ValidationError):
        SocioCreate(correo="c@c.com")

def test_socio_out_mapping():
    # Incluimos `correo` en los datos
    data = {"id": "S2", "nombre": "Luis", "correo": "l@l.com"}
    s_out = SocioOut(**data)
    assert s_out.id == "S2"
    assert s_out.nombre == "Luis"
    assert s_out.correo == "l@l.com"