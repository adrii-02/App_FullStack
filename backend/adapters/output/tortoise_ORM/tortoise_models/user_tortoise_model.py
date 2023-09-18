from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class User(Model):
    id= fields.IntField(pk=True)
    email = fields.CharField(max_length=100, nullable=False)
    name = fields.CharField(max_length=30, nullable=False)
    age = fields.IntField(nullable=False)
    length = fields.DecimalField(max_digits=4, decimal_places=2, nullable=False)
    weight = fields.DecimalField(max_digits=3, decimal_places=2, nullable=False)

    #Foreign Key
    #role = fields.ForeignKeyField('models.Role', related_name="roles")


# Pydantic Models
user_pydantic = pydantic_model_creator(User, name="User")
user_pydanticIn = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)