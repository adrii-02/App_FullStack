from fastapi import HTTPException, status
from backend.adapters.output.tortoise_ORM.tortoise_models.user_tortoise_model import User, user_pydantic, user_pydanticIn
from backend.application.repositories.user_repository import UserRepository
from backend.domain.models.status import Status

class TortoiseUserRepository(UserRepository):
    
    async def add_user(self, user_info: user_pydanticIn):
        user_obj = await User.create(**user_info.dict(exclude_unset=True))
        response = await user_pydantic.from_tortoise_orm(user_obj)
        return {"status":"ok", "data":response}

    async def get_users(self):
        response = await user_pydantic.from_queryset(User.all())
        return list(response)

    async def get_user_by_id(self, user_id: int):#REVISAR MÉTODO PORQUE NO VA
        user = await User.get(id=user_id)
        if user is not None:
            try:
                response = await user_pydantic.from_queryset_single(user)
                return {"status": "ok", "data": response}
            except Exception as e:
                print(f"Error converting to Pydantic: {e}")
        else:
            return {"status": "error", "message": "User not found"}

    async def update_user_by_id(self, user_id: int, update_info: user_pydanticIn):
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

    async def delete_user_by_id(self, user_id: int):
            delete_user = await User.filter(id=user_id).delete()
            if not delete_user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {user_id} not found in DB.')
            return Status(message=f'Deleted user {user_id}')
            