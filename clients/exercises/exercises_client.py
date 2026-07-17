from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий через id курса
    """
    courseId: str

class GetExercisesResponseDict(TypedDict):
    exercise:list[Exercise]



class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId:str
    maxScore: int | None
    minScore: int | None
    orderIndex:int
    description: str
    estimatedTime:str | None

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания задания.
    """
    exercise:Exercise


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на редактирование задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex:int | None
    description: str | None
    estimatedTime:str | None

class UpdateExerciseResponseDict(TypedDict):
    exercise:Exercise



class ExercisesClient(APIClient):
    """
    Клиент для работы с  /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict)-> Response:
        """
        Метод для получения списка заданий
        :param query: словарь с courseId
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises',params=query)

    def get_exercise_api(self,exercise_id:str)-> Response:
        """
        Метод для получения задания по exercise_id
        :param exercise_id: Идентификатор задания
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self,request:CreateExercisesRequestDict)-> Response:
        """
        Метод для создания заданий курса
        :param request: Словарь с title,courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises",json=request)

    def update_exercise_api(self,exercise_id:str, request: UpdateExerciseRequestDict)-> Response:
        """
        Метод для редактирования заданий курса
        :param exercise_id: Идентификатор задания
        :param request: Словарь с title,maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
         """
        return self.patch(f"/api/v1/exercises/{exercise_id}",json=request)

    def delete_exercise_api(self,exercise_id:str)-> Response:
        """
         Метод удаления заданий.

         :param exercise_id: Идентификатор задания.
         :return: Ответ от сервера в виде объекта httpx.Response
         """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id:str) -> GetExercisesResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request:CreateExercisesRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self,exercise_id:str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id,request)
        return response.json()

def get_exercises_client(user:AuthenticationUserSchema)-> ExercisesClient:
    """
       Функция создает экземпляр ExercisesClient с уже настроенным HTTP-клиентом

       :return: Готовый к использованию объект ExercisesClient
       """
    return ExercisesClient(client=get_private_http_client(user))