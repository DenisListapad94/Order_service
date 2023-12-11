from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from src.orders.router import router as router_order

app = FastAPI(
    title="Orders Service"
)

app.include_router(router_order)


@app.get("/index")
async def main_page() -> dict:
    return {"message": "Hello World"}


# @app.get("/index/{item_id}")
# async def main_page_with_items(item_id: int) -> dict:
#     return {"item_id": item_id}
#
#
# @app.get("/users")
# async def get_users() -> list:
#     return users
#
#
# @app.post("/add_user", response_model=List[Users])
# async def get_users(user: Users) -> list:
#     users.append(user.model_dump())
#     return users
