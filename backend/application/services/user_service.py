from backend.application.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def add_user(self, user_info: dict):
        # Validar y procesar los datos del usuario si es necesario
        return await self.user_repository.add_user(user_info)

    async def get_users(self):
        # Aplicar lógica de filtrado o procesamiento adicional si es necesario
        return await self.user_repository.get_users()

    async def get_user_by_id(self, user_id: int):
        # Realizar validaciones adicionales o lógica de negocio
        return await self.user_repository.get_user_by_id(user_id)

    async def update_user_by_id(self, user_id: int, update_info: dict):
        # Validar y procesar los datos de actualización
        return await self.user_repository.update_user_by_id(user_id, update_info)

    async def delete_user_by_id(self, user_id: int):
        # Validar permisos o realizar otras validaciones
        return await self.user_repository.delete_user_by_id(user_id)