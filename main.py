from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from app import app
import uvicorn, tracemalloc

tracemalloc.start()


register_tortoise(
     app,
     config={
            'connections': {
                # Dict format for connection
                'default': {
                    'engine': 'tortoise.backends.mysql',
                    'credentials': {
                        'host': 'localhost',
                        'port': '3306',
                        'user': 'root',
                        'password': '@Q7wG6#1$HJ4$',
                        'database': 'fullstacks',
                    }  
                }
            },
            'apps': {
                'models': {
                    'models' : [
                        'backend.adapters.output.tortoise_ORM.tortoise_models.user_tortoise_model'
                    ],
                    # If no default_connection specified, defaults to 'default'
                    'default_connection': 'default',
                }
            }
        }
)
# Using a DB_URL string -> 'default': f'mysql://root:{urlparse("@Q7wG6#1$HJ4$")}@localhost:3306/fullstacks'

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir cualquier método de solicitud (GET, POST, etc.)
    allow_headers=["*"],  # Permitir cualquier encabezado en la solicitud
)

Tortoise.generate_schemas()

uvicorn.run(app, host="127.0.0.1", port=8000)

# Debugging
'''
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
'''