from fastapi import APIRouter, Depends, status
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from database import get_async_session
from .models import DeliveryBoy, Order
from .schemas import (
    DeliveryBoyUpdateSchema,
    DeliveryBoySchema,
    DeliveryBoyCreateSchema,
    DeliveryBoyUpdatePartialSchema,
    OrderSchema
)
from .service import (
    create_delivery_boy,
    get_delivery_boys,
    update_delivery_boy,
    delete_delivery_boy
)
from .utils import get_delivery_boy_by_id

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/", response_model=DeliveryBoyCreateSchema, status_code=status.HTTP_201_CREATED)
async def create_boy(
        boy: DeliveryBoyCreateSchema,
        session: AsyncSession = Depends(get_async_session)
) -> DeliveryBoy:
    delivery_boy = await create_delivery_boy(boy=boy, session=session)
    return delivery_boy


@router.get("/", response_model=list[DeliveryBoySchema])
async def get_boys(
        session: AsyncSession = Depends(get_async_session),
) -> list[DeliveryBoy]:
    return await get_delivery_boys(session=session)


@router.get("/{boy_id}/", response_model=DeliveryBoySchema)
async def get_product(
        delivery_boy=Depends(get_delivery_boy_by_id)
) -> DeliveryBoy:
    return delivery_boy


@router.put("/{boy_id}/", response_model=DeliveryBoyUpdateSchema)
async def update_boy(
        boy: DeliveryBoyUpdateSchema,
        session: AsyncSession = Depends(get_async_session),
        delivery_boy=Depends(get_delivery_boy_by_id)
) -> DeliveryBoy:
    return await update_delivery_boy(
        session=session,
        delivery_boy=delivery_boy,
        delivery_object=boy,
    )


@router.patch("/{boy_id}/", response_model=DeliveryBoyUpdatePartialSchema)
async def update_partial_boy(
        boy: DeliveryBoyUpdatePartialSchema,
        session: AsyncSession = Depends(get_async_session),
        delivery_boy=Depends(get_delivery_boy_by_id)
) -> DeliveryBoy:
    return await update_delivery_boy(
        session=session,
        delivery_boy=delivery_boy,
        delivery_object=boy,
        partial=True
    )


@router.delete("/{boy_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_boy(
        session: AsyncSession = Depends(get_async_session),
        delivery_boy=Depends(get_delivery_boy_by_id)
) -> None:
    await delete_delivery_boy(
        session=session,
        delivery_boy=delivery_boy
    )


@router.post("/order", response_model=OrderSchema)
async def create_order(
        order_schema: OrderSchema,
        session: AsyncSession = Depends(get_async_session)
) -> Order:
    order = Order(**order_schema.model_dump())
    session.add(order)
    await session.commit()

    return order


@router.get("/orders", response_model=list[OrderSchema])
async def get_orders(
        session: AsyncSession = Depends(get_async_session),
) -> list[Order]:
    stmt = select(Order).order_by(Order.id)
    result: Result = await session.execute(stmt)
    orders = result.scalars().all()
    return list(orders)


# @router.get("/delivery_boy_orders")
# async def get_delivery_boy_orders(
#         session: AsyncSession = Depends(get_async_session),
# ):
    # query = (
    #     select(DeliveryBoy)
    #     .options(joinedload(DeliveryBoy.order))
    # )
    # query = (
    #     select(DeliveryBoy)
    #     .options(selectinload(DeliveryBoy.order))
    #     .filter(DeliveryBoy.age == 20)
    # )
    #
    # result: Result = await session.execute(query)
    #
    # delivery_boys = result.scalars().all()
    # for order in delivery_boys[0].order:
    #     print(order.items)
