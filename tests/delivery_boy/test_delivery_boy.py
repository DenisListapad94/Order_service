import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.anyio
async def test_create_delivery_boy(ac: AsyncClient):
    # import pdb;pdb.set_trace()
    # assert 1 == 1
    response = await ac.post("/orders", json={
        "id": 1,
        "name": "Jho",
        "fullname": "Philips",
        "age": 26,
    })
    assert response.status_code == 201

@pytest.mark.anyio
async def test_get_delivery_boy(ac: AsyncClient):
    response = await ac.get("/orders")

    assert response.status_code == 200
    # assert response.json()["status"] == "success"
    # assert len(response.json()["data"]) == 1
