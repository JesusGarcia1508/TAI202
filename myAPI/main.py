#importaciones
from fastapi import FastAPI

#instancia del servidor
app = FastAPI()

#Endpoint
@app.get("/")
async def holamundo():
    return {"mensaje":"Hola Mundo FastAPI"}

@app.get("/bienvenido")
async def bienvenido():
    return{
        "mensaje": "Bienvenido a FastAPI",
        "estatus" : "200",
    }