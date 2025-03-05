from sqlmodel import SQLModel, create_engine

DATABASE_URL = "mysql+mysqlconnector://root:Santiago2004@localhost:3306/4thewords_prueba_david_viloria"
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)