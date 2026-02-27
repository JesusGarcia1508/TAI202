from fastapi import FastAPI, HTTPException, status
from models import Libro, Usuario
from typing import List

app = FastAPI()

libros_db = []
prestamos_db = {}

@app.get("/")
def inicio():
    return {"mensaje": "Binevenido a la API de la Biblioteca Digital"}

#registrar un libro 
@app.post("/libros", status_code=201)
def registrar_libro(libro : Libro):
    if any(l.id == libro.id for l in libros_db):
        raise HTTPException(status_code=400, detail="El ID ya existe")
    libros_db.append(libro)
    return libro

#Listar todos los libros
@app.get("/libros", response_model=List[Libro])
def listar_libros():
    return libros_db

#Buscar libro por nombre
@app.get("/libros/buscar")
def buscar_libro(nombre: str):
    resultado = [l for l in libros_db if nombre.lower() in l.titulo.lower()]
    return resultado

#Registrar Prestamo (409 si ya esta prestado)
@app.post("/prestamos/{libro_id}")
def prestar_libro(libro_id: int, usuario: Usuario):
    for libro in libros_db:
        if libro.id == libro_id:
            if libro.estado == "prestado":
                raise HTTPException(status_code=409, detail="Conflict: El libro ya está prestado")
            libro.estado = "prestado"
            prestamos_db[libro_id] = usuario.nombre
            return {"mensaje": f"Préstamo registrado a {usuario.nombre}"}
        raise HTTPException(status_code=404, detail="Libro no encontrado")

#Marcar como devuelto (200 OK)
@app.put("/prestamos/devolver/{libro_id}")
def devolver_libro(libro_id : int):
    for libro in libro:
        if libro.id == libro_id:
            if libro_id not in prestamos_db:
                raise HTTPException(status_code=409, detail="Conflict: El registro de préstamo ya no existe")
            libro.estado = "disponible"
            del prestamos_db[libro_id]
            return {"mensaje": "200 OK: Libro devuelto"}
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
#Elminar registro de prestamo
@app.delete("/prestamos/{libro_id}")
def eliminar_prestamo(libro_id: int):
    if libro_id in prestamos_db:
        del prestamos_db[libro_id]
        return {"mensaje": "Registro eliminado"}
    raise HTTPException(status_code=404, datail="No existe el prestamo")

