# Backend - Libro de Leyendas
Este proyecto es una API desarrollada con FastAPI para gestionar leyendas típicas de Costa Rica. 
Permite crear, leer, actualizar y eliminar leyendas, almacenadas en una base de datos MySQL.

## Requisitos
- Python 3.8 o superior.
- MySQL instalado y en ejecución.

## Crea un entorno virtual y activa:
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

## Configura la base de datos:
Crea una base de datos en MySQL llamada 4thewords_prueba_nombre_apellido.
Ejecuta el script SQL proporcionado en la carpeta script para crear la tabla leyendas.

## Configura las credenciales de la base de datos:

Abre el archivo database/conexion.py
Modifica la variable DATABASE_URL con tus credenciales:
DATABASE_URL = "mysql+mysqlconnector://usuario:contraseña@localhost:3306/4thewords_prueba_nombre_apellido"

## Ejecución
Levanta el servidor de FastAPI:
uvicorn app.main:app --reload --port 8080

Accede a la documentación de la API:
Abre tu navegador y visita http://localhost:8080/docs.

Endpoints
Crear una leyenda: POST /leyendas/
Listar todas las leyendas: GET /leyendas/
Obtener una leyenda por ID: GET /leyendas/{leyenda_id}
Actualizar una leyenda: PUT /leyendas/{leyenda_id}
Eliminar una leyenda: DELETE /leyendas/{leyenda_id}

# Frontend - Libro de Leyendas
Este proyecto es el frontend de una aplicación para gestionar leyendas típicas de Costa Rica. Está desarrollado con Vue.js 3.

## Requisitos

- Node.js 14 o superior.

## Instala las dependencias:
npm install

## Ejecución
npm run dev






