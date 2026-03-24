#importaciones
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.data import usuario as usuarioDB
from app.router import usuario, misc
from app.data.db import engine

# Crear todas las tablas en la base de datos
usuarioDB.Base.metadata.create_all(bind=engine)

# Instancia del servidor
app = FastAPI(
    title="Mi API de Usuarios",
    description="API REST creada con FastAPI para gestionar usuarios. Incluye operaciones CRUD completas y autenticación HTTP Basic.",
    version="1.0.0",
    contact={
        "name": "Jesús Manuel García Seijas",
        "url": "http://localhost:5000/docs"
    },
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(usuario.router)
app.include_router(misc.misc)


