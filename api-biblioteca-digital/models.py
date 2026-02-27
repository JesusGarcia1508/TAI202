from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime

class Libro(BaseModel):
    id: int
    titulo: str = Field(..., min_length=2, max_length=100)
    autor : str
    paginas: int = Field(..., gt=1)
    anio : int = Field(..., gt=1450)
    estado : str = "disponible"

    @validator('anio')
    def validar_anio(cls, v):
        if v > datetime.now().year:
            raise ValueError('El año no puede ser mayor al actual')
        return v 
    
    @validator('estado')
    def validar_estado(cls, v):
        if v not in ["disponible", "prestado"]:
            raise ValueError('Estado debe ser "disponible" o "prestado"')
        return v
    
    class Usuario(BaseModel):
        nombre : str
        correo: EmailStr
        