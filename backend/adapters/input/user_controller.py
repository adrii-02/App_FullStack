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