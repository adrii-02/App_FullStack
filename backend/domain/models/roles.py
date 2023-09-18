'''
Tener instalado Tortoise ORM.
El comando que he utilizado para instalarlo es: py -m pip install tortoise-orm

from tortoise.models import Model
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Role(Model):
    id_client = fields.IntField(max=2, nullable=True)
    id_admin = fields.IntField(max=2, nullable=True)

role_pydantic = pydantic_model_creator(Role, name="roles")
role_pydanticIn = pydantic_model_creator(Role, name="rolesIn", exclude_readonly=True)
'''