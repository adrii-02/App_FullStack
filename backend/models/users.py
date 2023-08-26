'''
Tener instalado Tortoise ORM.
El comando que he utilizado para instalarlo es: py -m pip install tortoise-orm
'''
from tortoise.models import Model
from tortoise import fields

class Users(Model):
    id= fields.IntField(pk=True)
    admin = fields.BooleanField(nullable=False)
    email = fields.CharField(max_length=100, nullable=False)
    name = fields.CharField(max_length=30, nullable=False)
    age = fields.IntField(max_length=3, nullable=False)
    length = fields.DecimalField(max_digits=4, decimal_places=2, nullable=False)
    weight = fields.DecimalField(max_length=3, nullable=False)