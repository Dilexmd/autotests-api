from pydantic import BaseModel, Field


class ExerciseSchema(BaseModel):
    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий через id курса
    """
    courseId: str

class GetExercisesResponseSchema(BaseModel):
    exercise:list[ExerciseSchema]



class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str | None = Field(alias='estimatedTime')


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise:ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на редактирование задания.
    """
    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index:int | None = Field(alias='orderIndex')
    description: str | None
    estimatedTime:str | None = Field(alias='estimatedTime')


class UpdateExerciseResponseSchema(BaseModel):
    exercise:ExerciseSchema