from fastapi import APIRouter, HTTPException
from ..schemas.user_schema   import UserCreate, UserLogin, UserOut
from ..services.auth_service import register_user, authenticate_user

router = APIRouter()

# 1) Ruta de creación y listado primero (para que no pise la dinámica "/{socio_id}")

@router.post("/registrar", response_model=SocioOut)
async def registrar_socio_endpoint(socio: SocioCreate):
    """
    Endpoint para registrar un nuevo socio.
    """
    new_id = await crear_socio(socio)
    if not new_id:
        raise HTTPException(status_code=400, detail="Error al registrar socio")
    # Devolver exactamente los campos que espera SocioOut
    return SocioOut(
        id=new_id,
        nombre=socio.nombre,
        correo=socio.correo,
        telefono=socio.telefono,
        direccion=socio.direccion
    )

@router.get("/listar", response_model=list[SocioOut])
async def listar_socios_endpoint():
    """
    Endpoint para listar todos los socios registrados.
    """
    raw = await listar_socios()
    # raw es lista de dicts con al menos id,nombre,correo; los opcionales los rellena Pydantic
    return raw

# 2) Ahora la ruta dinámica

@router.get("/{socio_id}", response_model=SocioOut)
async def obtener_socio_endpoint(socio_id: str):
    """
    Endpoint para obtener los detalles de un socio.
    """
    socio = await obtener_socio_por_id(socio_id)
    if not socio:
        raise HTTPException(status_code=404, detail="Socio no encontrado")
    return socio

@router.put("/{socio_id}", response_model=SocioOut)
async def actualizar_socio_endpoint(socio_id: str, socio: SocioCreate):
    """
    Endpoint para actualizar la información de un socio.
    """
    ok = await modificar_socio(socio_id, socio.dict())
    if not ok:
        raise HTTPException(status_code=400, detail="No se pudo actualizar el socio")
    return await obtener_socio_por_id(socio_id)

@router.delete("/{socio_id}", response_model=dict)
async def eliminar_socio_endpoint(socio_id: str):
    """
    Endpoint para eliminar un socio.
    """
    ok = await eliminar_socio_por_id(socio_id)
    if not ok:
        raise HTTPException(status_code=400, detail="No se pudo eliminar el socio")
    return {"message": "Socio eliminado exitosamente"}
