from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id:int
    name:str
    email: str
    is_active: bool = Field(alias="isActive")

user = User(
    id=1,
    name="Alice",
    email="alice@example.com",
    address= {'city':'MSK', "zip_code":'111111'}
)
print(user)