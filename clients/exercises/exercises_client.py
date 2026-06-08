from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict


class GetExersiceQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий через id курса
    """
    courseId : str

class CreateExersiceQueryDict(TypedDict):
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

class UpdateExersiceRequestDict(TypedDict):
    """
    Описание структуры запроса на редактирование задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex:int | None
    description: str | None
    estimatedTime:str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с  /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExersiceQueryDict)-> Response:
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

    def create_exercise_api(self,request:CreateExersiceQueryDict)-> Response:
        """
        Метод для создания заданий курса
        :param request: Словарь с title,courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises",json=request)

    def update_exercise_api(self,exercise_id:str, request: UpdateExersiceRequestDict)-> Response:
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