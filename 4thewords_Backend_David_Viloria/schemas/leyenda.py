from pydantic import BaseModel
from datetime import date

class LeyendaCreate(BaseModel):
    nombre: str
    categoria: str
    descripcion: str
    fecha: date
    provincia: str
    canton: str
    distrito: str
    imagen_url: str

class LeyendaRead(BaseModel):
    id: int
    nombre: str
    categoria: str
    descripcion: str
    fecha: date
    provincia: str
    canton: str
    distrito: str
    imagen_url: str