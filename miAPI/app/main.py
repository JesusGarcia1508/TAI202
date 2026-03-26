from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.data import usuario as usuarioDB
from app.router import usuario, misc
from app.data.db import engine

usuarioDB.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Usuarios",
    description="REST API para gestión de usuarios con operaciones CRUD y autenticación.",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario.router)
app.include_router(misc.misc)


