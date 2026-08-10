import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExercisesRequestSchema
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    response : CreateExerciseResponseSchema
    request : CreateExercisesRequestSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(exercises_client: ExercisesClient) -> ExerciseFixture:
    request = CreateExercisesRequestSchema()
    response = exercises_client.create_exercise(request)
    return  ExerciseFixture(response=response, request=request)