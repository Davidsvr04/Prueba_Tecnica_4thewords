from sqlmodel import Session, select
from database.conexion import engine
from models.leyenda import Leyendas

def test_connection():
  try:
    with Session(engine) as session:
        print("¡Conexión exitosa!")
        leyendas = session.exec(select(Leyendas)).all()
        if leyendas:
            print("Leyendas encontradas:")
            for leyenda in leyendas:
                print(leyenda)
        else:
            print("No se encontraron leyendas en la base de datos.")
  except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == "__main__":
  test_connection()