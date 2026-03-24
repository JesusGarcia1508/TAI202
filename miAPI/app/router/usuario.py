from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from app.models.usuario import crear_usuario
from sqlalchemy.orm import Session
from app.data.db import get_db
from app.data.usuario import usuario as dbUsuario
from app.security.auth import verificar_peticion

router = APIRouter(
    prefix="/v1/usuarios",
    tags=["CRUD Usuarios"]
)

#*********************
# Usuario CRUD
#*********************
@router.get(
    "/",
    summary="Obtener todos los usuarios",
    description="Retorna una lista de todos los usuarios registrados en la base de datos",
    response_description="Lista de usuarios con su ID, nombre y edad"
)
async def leer_usuarios(db: Session = Depends(get_db)):
    """
    **GET /v1/usuarios/**
    
    Obtiene la lista completa de usuarios.
    
    **Retorna:**
    - status: Código de estado HTTP
    - total: Cantidad total de usuarios
    - usuarios: Lista de objetos usuario
    """
    queryUsuarios = db.query(dbUsuario).all()
    return {
        "status": "200",
        "total": len(queryUsuarios),
        "usuarios": queryUsuarios
    }


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo usuario",
    description="Crea un nuevo usuario en la base de datos con nombre y edad",
    response_description="Confirmación de creación con los datos del nuevo usuario"
)
async def crear_usuario_endpoint(usuarioP: crear_usuario, db: Session = Depends(get_db)):

    nuevoU = dbUsuario(nombre=usuarioP.nombre, edad=usuarioP.edad)
    db.add(nuevoU)
    db.commit()
    db.refresh(nuevoU)

    return {
        "mensaje": "Usuario Creado",
        "Datos nuevos": usuarioP
    }


@router.put(
    "/{id}",
    summary="Actualizar usuario completo",
    description="Reemplaza todos los datos de un usuario existente",
    response_description="Usuario actualizado correctamente"
)
async def actualizar_usuario(id: int, usuario_actualizado: crear_usuario, db: Session = Depends(get_db)):
    """
    **PUT /v1/usuarios/{id}**
    
    Actualiza completamente un usuario (reemplaza todos sus datos).
    
    **Parámetros:**
    - id: ID del usuario a actualizar
    - nombre: Nuevo nombre
    - edad: Nueva edad
    
    **Retorna:**
    - mensaje: Confirmación de actualización
    - datos_nuevos: Usuario actualizado
    """
    usuarioDb = db.query(dbUsuario).filter(dbUsuario.id == id).first()
    if not usuarioDb:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado para actualizar"
        )
    usuarioDb.nombre = usuario_actualizado.nombre
    usuarioDb.edad = usuario_actualizado.edad
    db.commit()
    db.refresh(usuarioDb)
    return {
        "mensaje": "Usuario actualizado correctamente",
        "datos_nuevos": usuarioDb,
        "status": "200"
    }


@router.patch(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Actualización parcial",
    description="Modifica solo los campos especificados de un usuario",
    response_description="Usuario modificado parcialmente"
)
async def actualizar_parcial_usuario(id: int, usuario_parcial: dict, db: Session = Depends(get_db)):
    """
    **PATCH /v1/usuarios/{id}**
    
    Actualiza parcialmente un usuario (solo los campos enviados).
    
    **Parámetros:**
    - id: ID del usuario a modificar
    - usuario_parcial: Diccionario con los campos a actualizar
    
    **Retorna:**
    - mensaje: Confirmación de modificación
    - datos_nuevos: Usuario modificado
    """
    usuarioDb = db.query(dbUsuario).filter(dbUsuario.id == id).first()
    if not usuarioDb:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado para modificar"
        )
    for campo, valor in usuario_parcial.items():
        if hasattr(usuarioDb, campo) and campo != "id":
            setattr(usuarioDb, campo, valor)
    db.commit()
    db.refresh(usuarioDb)
    return {
        "mensaje": "Usuario modificado parcialmente",
        "datos_nuevos": usuarioDb,
        "status": "200"
    }


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar un usuario",
    description="Elimina un usuario de la base de datos (requiere autenticación)",
    response_description="Confirmación de eliminación"
)
async def eliminar_usuario(id: int, db: Session = Depends(get_db), usuarioAuth: str = Depends(verificar_peticion)):
    """
    **DELETE /v1/usuarios/{id}**
    
    Elimina un usuario (requiere autenticación HTTP Basic).
    
    **Parámetros:**
    - id: ID del usuario a eliminar
    - Autenticación: usuario "jesus" / contraseña "123456"
    
    **Retorna:**
    - mensaje: Confirmación de eliminación
    - usuario_eliminado: Datos del usuario eliminado
    """
    usuarioDb = db.query(dbUsuario).filter(dbUsuario.id == id).first()
    if not usuarioDb:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado para eliminar"
        )
    db.delete(usuarioDb)
    db.commit()
    return {
        "mensaje": f"Usuario eliminado por {usuarioAuth}",
        "usuario_eliminado": usuarioDb,
        "status": "200"
    }