'''
Para encender el servidor, hay que tener instalado en el dispositivo el servidor uvicorn.
Una vez instalado pondremos el siguiente comando para ponerlo en marcha: py -m uvicorn app:app --reload
'''

from fastapi import FastAPI, HTTPException, status
from tortoise.contrib.fastapi import register_tortoise
from domain.models.users import user_pydantic, user_pydanticIn, User
from domain.models.status import Status

app = FastAPI()



@app.get('/')
def index():
    return {"Msg":"Go to /docs for the API documentation"}



@app.post('/user')
async def add_user(user_info: user_pydanticIn):
    user_obj = await User.create(**user_info.dict(exclude_unset=True))
    response = await user_pydantic.from_tortoise_orm(user_obj)
    return {"status":"ok", "data":response}

@app.get('/users')
async def get_users():
    response = await user_pydantic.from_queryset(User.all())
    return {"status":"ok", "data":response}

@app.get('/user/{user_id}')
async def get_user_by_id(user_id: int):
    response = await user_pydantic.from_queryset_single(User.get(id = user_id))
    return {"status":"ok", "data":response}

@app.put('/user/{user_id}')
async def update_user_by_id(user_id: int, update_info: user_pydanticIn):
    user_obj = await User.get(id = user_id)
    update_info = update_info.dict(exclude_unset=True)

    user_obj.email = update_info['email']
    user_obj.name = update_info['name']
    user_obj.age = update_info['age']
    user_obj.length = update_info['length']
    user_obj.weight = update_info['weight']
    await user_obj.save()

    response = await user_pydantic.from_tortoise_orm(user_obj)
    return {"status":"ok", "data":response}

@app.delete('/user/{user_id}')
async def delete_user_by_id(user_id: int):
        delete_user = await User.filter(id=user_id).delete()
        if not delete_user:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {user_id} not found in DB.')
        return Status(message=f'Deleted user {user_id}')


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
                        'domain.models.roles',
                        'domain.models.users'
                    ],
                    # If no default_connection specified, defaults to 'default'
                    'default_connection': 'default',
                }
            }
        }
)
# Using a DB_URL string -> 'default': f'mysql://root:{urlparse("@Q7wG6#1$HJ4$")}@localhost:3306/fullstacks'