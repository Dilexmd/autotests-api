import httpx


# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print(response.status_code)
# print(response.json())



# data = {
#     "title":'Новая задача',
#     "completed": False,
#     "userId": 1
# }
# response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
# print(response.status_code)
# print(response.headers)
# print(response.json())



# data = {"username": "test_user",
#         "password": "12345"
#         }
# response = httpx.post("https://httpbin.org/post", data=data)
# print(response.status_code)
# print(response.headers)
# print(response.json())



# headers = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
# print(response.request.headers)
# print(response.json())



# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# print(response.url)
# print(response.json())



# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
# print(response.json())  # Ответ с данными о загруженном файле



# with httpx.Client() as clients:
#     response1 = clients.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = clients.get("https://jsonplaceholder.typicode.com/todos/2")
# print(response1.json())  # Данные первой задачи
# print(response2.json())  # Данные второй задачи



# clients = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
# response = clients.get("https://httpbin.org/get")
# print(response.json())  # Заголовки включены в ответ
# clients.close()



# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()  # Вызовет исключение при 4xx/5xx
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка запроса: {e}")



# try:
#     response = httpx.get("https://httpbin.org/delay/5", timeout=2)
# except httpx.ReadTimeout:
#     print("Запрос превысил лимит времени")