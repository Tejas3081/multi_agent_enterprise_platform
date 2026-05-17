from fastapi import APIRouter, WebSocket

socket_router = APIRouter()

@socket_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    while True:

        data = await websocket.receive_text()

        await websocket.send_text(
            f"Agent Response: {data}"
        )