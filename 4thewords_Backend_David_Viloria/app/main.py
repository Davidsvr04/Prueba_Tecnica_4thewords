from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from database.conexion import engine, create_db_and_tables
from models.leyenda import Leyendas
from schemas.leyenda import LeyendaCreate, LeyendaRead

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/leyenda/", response_model=LeyendaRead)
def crear_leyenda(leyenda: LeyendaCreate):
    with Session(engine) as session:
        db_leyenda = Leyendas(**leyenda.dict())
        session.add(db_leyenda)
        session.commit()
        session.refresh(db_leyenda)
        return db_leyenda
    
@app.get("/leyenda/", response_model=list[LeyendaRead])
def listar_leyendas():
    with Session(engine) as session:
        leyendas = session.exec(select(Leyendas)).all()
        return leyendas
    
@app.get("/leyenda/{leyenda_id}", response_model=LeyendaRead)
def obtener_leyenda(leyenda_id: int):
    with Session(engine) as session:
        leyenda = session.get(Leyendas, leyenda_id)
        if not leyenda:
            raise HTTPException(status_code=404, detail="Leyenda no encontrada")
        return leyenda
    
@app.put("/leyenda/{leyenda_id}", response_model=LeyendaRead)
def actualizar_leyenda(leyenda_id: int, leyenda: LeyendaCreate):
    with Session(engine) as session:
        db_leyenda = session.get(Leyendas, leyenda_id)
        if not db_leyenda:
            raise HTTPException(status_code=404, detail="Leyenda no encontrada")
        for key, value in leyenda.dict().items():
            setattr(db_leyenda, key, value)
        session.commit()
        session.refresh(db_leyenda)
        return db_leyenda
    
@app.delete("/leyenda/{leyenda_id}")
def eliminar_leyenda(leyenda_id: int):
    with Session(engine) as session:
        db_leyenda = session.get(Leyendas, leyenda_id)
        if not db_leyenda:
            raise HTTPException(status_code=404, detail="Leyenda no encontrada")
        session.delete(db_leyenda)
        session.commit()
        return {"mensaje": "Leyenda eliminada"}