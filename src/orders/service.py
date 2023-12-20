"""
Create
Read
Update
UpdatePartial
Delete

"""
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.orders.models import DeliveryBoy
from src.orders.schemas import DeliveryBoyCreateSchema, DeliveryBoyUpdateSchema, DeliveryBoyUpdatePartialSchema


async def create_delivery_boy(
        session: AsyncSession,
        boy: DeliveryBoyCreateSchema,
) -> DeliveryBoy:
    delivery_boy = DeliveryBoy(**boy.model_dump())
    session.add(delivery_boy)
    await session.commit()

    return delivery_boy


async def get_delivery_boys(session: AsyncSession) -> list[DeliveryBoy]:
    stmt = select(DeliveryBoy).order_by(DeliveryBoy.id)
    result: Result = await session.execute(stmt)
    delivery_boys = result.scalars().all()
    return list(delivery_boys)


async def get_delivery_boy(session: AsyncSession, delivery_boy_id: int) -> DeliveryBoy | None:
    return await session.get(DeliveryBoy, delivery_boy_id)


async def update_delivery_boy(
        session: AsyncSession,
        delivery_boy: DeliveryBoy,
        delivery_object: DeliveryBoyUpdateSchema,
) -> DeliveryBoy:
    for name, value in delivery_object.model_dump().items():
        setattr(delivery_boy, name, value)
    await session.commit()
    return delivery_boy


async def update_partial_delivery_boy(
        session: AsyncSession,
        delivery_boy: DeliveryBoy,
        delivery_object: DeliveryBoyUpdatePartialSchema,
        partial: bool,
) -> DeliveryBoy:
    for name, value in delivery_object.model_dump(exclude_unset=partial).items():
        setattr(delivery_boy, name, value)
    await session.commit()
    return delivery_boy



async def delete_delivery_boy(
        session: AsyncSession,
        delivery_boy: DeliveryBoy,
) -> None:
    await session.delete(delivery_boy)
    await session.commit()
