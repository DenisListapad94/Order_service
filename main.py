from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Users(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    sex: str | None

users = [
    {
        "id": 1,
        "name": "Tom",
        "surname": "Hanks",
        "age": 54,
        "sex": "m"
    },
    {
        "id": 2,
        "name": "Nick",
        "surname": "Poup",
        "age": 30,
        "sex": "m"
    },
    {
        "id": 3,
        "name": "Anna",
        "surname": "Watson",
        "age": 25,
        "sex": "f"
    }

]


@app.get("/index")
async def main_page() -> dict:
    return {"message": "Hello World"}


@app.get("/index/{item_id}")
async def main_page_with_items(item_id: int) -> dict:
    return {"item_id": item_id}


@app.get("/users")
async def get_users() -> list:
    return users


@app.post("/add_user",response_model= List[Users])
async def get_users(user: Users) -> list:
    users.append(user.model_dump())
    return users
