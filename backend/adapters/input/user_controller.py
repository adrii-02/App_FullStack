from fastapi import APIRouter, HTTPException, status
from backend.application.services.user_service import UserService
from backend.adapters.output.tortoise_ORM.tortoise_repositories.tortoise_user_repository import TortoiseUserRepository
from backend.domain.models.status import Status
from backend.adapters.output.tortoise_ORM.tortoise_models.user_tortoise_model import User, user_pydanticIn

router = APIRouter(prefix="/user", tags=["user"], responses={404: {"description": "Not Found"}})
user_repository = TortoiseUserRepository()
user_service = UserService(user_repository)



@router.post('/')
async def add_user(user_info: user_pydanticIn):
    try:
         response = await user_service.add_user(user_info)
         return {"status":"ok", "data":response}
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get('/')
async def get_users():
    try:
        response = await user_service.get_users()
        return list(response)
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get('/{user_id}')
async def get_user_by_id(user_id: int):
    try:
        response = await user_service.get_user_by_id(user_id=user_id)
        return User(response)
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.put('/{user_id}')
async def update_user_by_id(user_id: int, update_info: user_pydanticIn):
    try:
        response = await user_service.update_user_by_id(user_id=user_id, update_info=update_info)
        return {"status":"ok", "data":response}
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

@router.delete('/{user_id}')
async def delete_user_by_id(user_id: int):
    try:    
        response = await user_service.delete_user_by_id(user_id=user_id)
        return {"status":"ok", "data":response}
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

'''
@router.post('/')
async def add_user(user_info: user_pydanticIn):
    user_obj = await User.create(**user_info.dict(exclude_unset=True))
    response = await user_pydantic.from_tortoise_orm(user_obj)
    return {"status":"ok", "data":response}

@router.get('/')
async def get_users():
    response = await user_pydantic.from_queryset(User.all())
    return {"status":"ok", "data":response}

@router.get('/{user_id}')
async def get_user_by_id(user_id: int):
    response = await user_pydantic.from_queryset_single(User.get(id = user_id))
    return {"status":"ok", "data":response}

@router.put('/{user_id}')
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

@router.delete('/{user_id}')
async def delete_user_by_id(user_id: int):
        delete_user = await User.filter(id=user_id).delete()
        if not delete_user:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {user_id} not found in DB.')
        return Status(message=f'Deleted user {user_id}')
'''