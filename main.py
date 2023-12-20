from fastapi import FastAPI

from src.orders.router import router as router_order

app = FastAPI(
    title="Orders Service",
)

app.include_router(router_order)


@app.get("/index")
async def main_page() -> dict:
    return {"message": "Hello World"}


