from pydantic import BaseModel, Field, EmailStr, UUID4, constr

"""
Модель для валидации /api/v1/users
"""

class UserSchema(BaseModel):
    """
    Схема данных пользователя.

    id: Уникальный идентификатор пользователя
    email: Электронная почта пользователя
    last_name: Фамилия пользователя
    first_name: Имя пользователя
    middle_name: Отчество пользователя
    """

    id: UUID4
    email: EmailStr = Field(min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50) = Field(alias='lastName')
    first_name: constr(min_length=1, max_length=50) = Field(alias='firstName')
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):

    """
    Схема запроса на создание пользователя.

    email: Электронная почта пользователя
    password: Пароль пользователя
    last_name: Фамилия пользователя
    first_name: Имя пользователя
    middle_name: Отчество пользователя
    """

    email: EmailStr = Field(min_length=1, max_length=250)
    password: constr(min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50) = Field(alias='lastName')
    first_name: constr(min_length=1, max_length=50) = Field(alias='firstName')
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа созданного пользователя.

    user: Объект с данными созданного пользователя

    """
    user: UserSchema