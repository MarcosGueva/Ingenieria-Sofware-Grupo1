import pytest
from services import credito_service as cs

@pytest.mark.asyncio
async def test_registrar_credito(monkeypatch):
    # Stub de modelo de crédito y repo
    fake_input = {"monto": 1000, "tasa": 0.1, "plazo": 12}
    expected_id = "cred123"

    async def fake_registrar(data):
        assert data == fake_input
        return expected_id

    # Parchea la llamada interna al repositorio
    monkeypatch.setattr(cs, "registrar_credito", fake_registrar)

    # Llama al servicio
    new_id = await cs.registrar_credito(fake_input)
    assert new_id == expected_id

@pytest.mark.asyncio
async def test_solicitar_credito(monkeypatch):
    credit_data = {"socio_id": "S1", "monto": 500}
    expected_ok = True

    async def fake_solicitar(data):
        assert data == credit_data
        return expected_ok

    monkeypatch.setattr(cs, "solicitar_credito", fake_solicitar)

    result = await cs.solicitar_credito(credit_data)
    assert result is expected_ok

@pytest.mark.asyncio
async def test_obtener_credito(monkeypatch):
    cred_id = "cred123"
    fake_credito = {"_id": cred_id, "monto": 1000}

    async def fake_obtener(cid):
        assert cid == cred_id
        return fake_credito

    monkeypatch.setattr(cs, "obtener_credito", fake_obtener)

    credito = await cs.obtener_credito(cred_id)
    assert credito["_id"] == cred_id

@pytest.mark.asyncio
async def test_obtener_historial_creditos(monkeypatch):
    socio_id = "S1"
    fake_historial = [{"_id": "c1"}, {"_id": "c2"}]

    async def fake_hist(sid):
        assert sid == socio_id
        return fake_historial

    monkeypatch.setattr(cs, "obtener_historial_creditos", fake_hist)

    historial = await cs.obtener_historial_creditos(socio_id)
    assert isinstance(historial, list)
    assert len(historial) == 2

@pytest.mark.asyncio
async def test_aprobar_credito(monkeypatch):
    cred_id = "cred123"
    fake_status = {"_id": cred_id, "aprobado": True}

    async def fake_aprobar(cid):
        assert cid == cred_id
        return fake_status

    monkeypatch.setattr(cs, "aprobar_credito", fake_aprobar)

    status = await cs.aprobar_credito(cred_id)
    assert status["aprobado"] is True

@pytest.mark.asyncio
async def test_aprobar_credito_solicitado(monkeypatch):
    cred_id = "cred123"
    fake_resp = {"_id": cred_id, "solicitud_aprobada": True}

    async def fake_aprobar_solicitud(cid):
        assert cid == cred_id
        return fake_resp

    monkeypatch.setattr(cs, "aprobar_credito_solicitado", fake_aprobar_solicitud)

    resp = await cs.aprobar_credito_solicitado(cred_id)
    assert resp["solicitud_aprobada"] is True
