import asyncio
import websockets


async def client():
    uri = "ws://localhost:8765"
    async  with websockets.connect(uri) as websocket:
        message = "Привет, Сервер!"
        print(f'Отправка: {message}')
        await websocket.send(message)

        for n in range(6):
            message = await websocket.recv()
            print(message)


asyncio.run(client())