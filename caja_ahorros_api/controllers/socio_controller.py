from fastapi import APIRouter, HTTPException
from schemas.socio_schema import SocioCreate, SocioOut
from services.socio_service import crear_socio, obtener_socio_por_id, modificar_socio, eliminar_socio_por_id, listar_socios

router = APIRouter()

@router.post("/registrar", response_model=SocioOut)
async def registrar_socio_endpoint(socio: SocioCreate):
    """
    Endpoint para registrar un nuevo socio.
    """
    socio_id = await crear_socio(socio)
    if not socio_id:
        raise HTTPException(status_code=400, detail="Error al registrar socio")
    return {"socio_id": socio_id}

@router.get("/{socio_id}", response_model=SocioOut)
async def obtener_socio_endpoint(socio_id: str):
    """
    Endpoint para obtener los detalles de un socio.
    """
    socio = await obtener_socio_por_id(socio_id)
    return socio

@router.put("/{socio_id}", response_model=SocioOut)
async def actualizar_socio_endpoint(socio_id: str, socio: SocioCreate):
    """
    Endpoint para actualizar la información de un socio.
    """
    actualizado = await modificar_socio(socio_id, socio.dict())
    if not actualizado:
        raise HTTPException(status_code=400, detail="No se pudo actualizar el socio")
    return await obtener_socio_por_id(socio_id)

@router.delete("/{socio_id}", response_model=dict)
async def eliminar_socio_endpoint(socio_id: str):
    """
    Endpoint para eliminar un socio.
    """
    eliminado = await eliminar_socio_por_id(socio_id)
    if not eliminado:
        raise HTTPException(status_code=400, detail="No se pudo eliminar el socio")
    return {"message": "Socio eliminado exitosamente"}

@router.get("/listar", response_model=list[SocioOut])
async def listar_socios_endpoint():
    """
    Endpoint para listar todos los socios registrados.
    """
    socios = await listar_socios()
    return socios
