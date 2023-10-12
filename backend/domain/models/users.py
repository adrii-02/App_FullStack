'''
Tener instalado Tortoise ORM.
El comando que he utilizado para instalarlo es: py -m pip install tortoise-orm
'''
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class User():
    def __init__(self, id:int, email:str, name:str, age:int, length:float, weight:float):
        self.id = id,
        self.email = email,
        self.name = name,
        self.age = age,
        self.length = length,
        self.weight = weight,

    #Foreign Key
    #role = fields.ForeignKeyField('models.Role', related_name="roles")