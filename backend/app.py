'''
Para encender el servidor, hay que tener instalado en el dispositivo el servidor uvicorn.
Una vez instalado pondremos el siguiente comando para ponerlo en marcha: py -m uvicorn app:app --reload
'''

from fastapi import FastAPI

app = FastAPI()

app.get('/')
def index():
    return {"Msg":"Hello World"}