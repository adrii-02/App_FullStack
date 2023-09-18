from abc import ABC, abstractmethod
#from backend.adapters.output.tortoise_ORM.tortoise_models.user_tortoise_model import User
from typing import Optional, Dict

class UserRepository(ABC):
    @abstractmethod
    async def add_user(self, user_info: dict) -> Optional[Dict]:
        pass

    @abstractmethod
    async def get_users(self) -> any:
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> any:
        pass

    @abstractmethod
    async def update_user_by_id(self, user_id: int, update_info: dict) -> Optional[Dict]:
        pass

    @abstractmethod
    async def delete_user_by_id(self, user_id: int) -> Optional[Dict]:
        pass
