from pydantic import BaseModel, field_validator,PositiveInt

from enums import Gender


class Breed(BaseModel):
    name: str


class Cat(BaseModel):
    name: str
    age: PositiveInt
    gender: Gender
    breed: Breed
