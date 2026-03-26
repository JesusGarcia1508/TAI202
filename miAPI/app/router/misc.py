import asyncio
from typing import Optional
from app.data.database import usuarios
from fastapi import APIRouter

misc = APIRouter(tags=["Utilidades y Pruebas"])

@misc.get(
    "/",
    summary="Endpoint de prueba",
    description="Endpoint básico para verificar que la API está funcionando"
)
async def holamundo():
    return {"mensaje": "Hola Mundo FastAPI"}


@misc.get(
    "/bienvenido",
    summary="Bienvenida con espera",
    description="Endpoint que simula un procesamiento con espera de 5 segundos"
)
async def bienvenido():
    await asyncio.sleep(5)
    return {
        "mensaje": "Bienvenido a FastAPI",
        "estatus": "200",
    }


@misc.get(
    "/v1/parametroOb/{id}",
    summary="Búsqueda por parámetro obligatorio",
    description="Encuentra un usuario por su ID (parámetro obligatorio en la ruta)"
)
async def consultauno(id: int):
    return {
        "mensaje": "usuario encontrado",
        "usuario": id,
        "status": "200"
    }


@misc.get(
    "/v1/parametroOp/",
    summary="Búsqueda por parámetro opcional",
    description="Encuentra un usuario por su ID (parámetro opcional en query)"
)
async def consultatodos(id: Optional[int] = None):
    if id is not None:
        for usuarioK in usuarios:
            if usuarioK["id"] == id:
                return {"mensaje": "usuario encontrado", "usuario": usuarioK}
        return {"mensaje": "usuario no encontrado", "status": "200"}
    else:
        return {
            "mensaje": "Usuarios disponibles",
            "total": len(usuarios),
            "usuarios": usuarios,
            "status": "200"
        }