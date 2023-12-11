from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import DeliveryBoy
from .schemas import DeliveryBoySchema

router = APIRouter(
    prefix="/orders",
)


@router.get("/")
def get_orders():
    return {"status code": 200}


@router.post("create/", response_model=DeliveryBoySchema)
async def create_delivery_boy(
        boy: DeliveryBoySchema,
        session: AsyncSession = Depends(get_async_session)
) -> DeliveryBoy:
    delivery_boy = DeliveryBoy(
        id=boy.id,
        name=boy.name,
        fullname=boy.fullname,
        age=boy.age
    )
    session.add(delivery_boy)
    await session.commit()
    await session.refresh(delivery_boy)
    return delivery_boy
