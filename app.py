'''
Para encender el servidor, hay que tener instalado en el dispositivo el servidor uvicorn.
Una vez instalado pondremos el siguiente comando para ponerlo en marcha: py -m uvicorn app:app --reload
'''

from fastapi import FastAPI
from backend.adapters.input import user_controller

app = FastAPI()

# Rutas de la aplicación
app.include_router(user_controller.router)

@app.get('/')
def index():
    return {"Msg":"Go to /docs for the API documentation"}