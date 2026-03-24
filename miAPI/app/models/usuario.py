from pydantic import BaseModel, Field
from typing import Optional


#****************************
#Modelo de Validación usuario
#****************************

class crear_usuario(BaseModel):
    """Modelo para crear o actualizar un usuario"""
    id: Optional[int] = Field(None, gt=0, description="Identificador de usuario (auto-generado, opcional)")
    nombre: str = Field(..., min_length=3, max_length=50, example="Pepe", description="Nombre del usuario")
    edad: int = Field(..., ge=1, le=123, description="Edad válida entre 1 y 123 años")


class usuario_respuesta(BaseModel):
    """Modelo de respuesta de usuario"""
    id: int
    nombre: str
    edad: int

    class Config:
        from_attributes = True

