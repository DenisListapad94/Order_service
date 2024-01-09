from fastapi import APIRouter, Request, Depends
from fastapi import WebSocket
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates
from starlette.websockets import WebSocketDisconnect

from database import get_async_session
from .manager import manager
from .models import Message

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


#
# @router.get("/", response_class=HTMLResponse)
# async def get(request: Request):
#     return templates.TemplateResponse("chat.html", {"request": request})


# @router.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")
#
# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: list[WebSocket] = []
#
#     async def connect(self, websocket: WebSocket):
#         await websocket.accept()
#         self.active_connections.append(websocket)
#
#     def disconnect(self, websocket: WebSocket):
#         self.active_connections.remove(websocket)
#
#     async def send_personal_message(self, message: str, websocket: WebSocket):
#         await websocket.send_text(message)
#
#     async def broadcast(self, message: str, add_to_db: bool):
#         # if add_to_db:
#         #     await self.add_messages_to_database(message)
#         for connection in self.active_connections:
#             await connection.send_text(message)
#
#     # @staticmethod
#     # async def add_messages_to_database(message: str):
#     #     async with async_session_maker() as session:
#     #         stmt = insert(Message).values(
#     #             message=message
#     #         )
#     #         await session.execute(stmt)
#     #         await session.commit()
#
#
# manager = ConnectionManager()
#
#
# @router.websocket("/ws/{client_id}")
# async def websocket_endpoint(websocket: WebSocket, client_id: int):
#     await manager.connect(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await manager.broadcast(f"Client #{client_id} says: {data}", add_to_db=True)
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         await manager.broadcast(f"Client #{client_id} left the chat", add_to_db=False)


@router.get("/")
async def get(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse(name="chat.html", context=context)


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int,
                             session: AsyncSession = Depends(get_async_session), ):
    await manager.connect(websocket)
    try:
        stmt = select(Message).limit(5)
        result = await session.execute(stmt)
        messages = result.scalars().all()
        verbose = [message.message for message in messages]
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"{verbose}", websocket)
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        # await manager.broadcast(f"Client #{client_id} left the chat")
