from fastapi import FastAPI


from src.chat.router import router as router_chat
from src.orders.router import router as router_order

from fastapi.testclient import TestClient

app = FastAPI(
    title="Orders Service",
)

app.include_router(router_order)
app.include_router(router_chat)


@app.get("/index")
async def main_page() -> dict:
    return {"message": "Hello World"}

# client = TestClient(app)
# def test_read_main():
#     response = client.get("/index")
#     import pdb; pdb.set_trace()
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello World"}




