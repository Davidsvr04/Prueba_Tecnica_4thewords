from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import date

class Leyendas(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    categoria: str
    descripcion: str
    fecha: date
    provincia: str
    canton: str
    distrito: str
    imagen_url: str