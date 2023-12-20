from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import DeliveryBoy
from .schemas import (
    DeliveryBoyUpdateSchema,
    DeliveryBoySchema,
    DeliveryBoyCreateSchema,
    DeliveryBoyUpdatePartialSchema
)
from .service import (
    create_delivery_boy,
    get_delivery_boys,
    get_delivery_boy,
    update_delivery_boy,
    update_partial_delivery_boy,
    delete_delivery_boy
)

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
        boy_id: int,
        session: AsyncSession = Depends(get_async_session),

) -> DeliveryBoy:
    delivery_boy = await get_delivery_boy(delivery_boy_id=boy_id, session=session)
    if not delivery_boy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Delivery boy {boy_id} not found!",
        )
    return delivery_boy


@router.put("/{boy_id}/", response_model=DeliveryBoyUpdateSchema)
async def update_boy(
        boy_id: int,
        boy: DeliveryBoyUpdateSchema,
        session: AsyncSession = Depends(get_async_session),
) -> DeliveryBoy:
    delivery_boy = await get_delivery_boy(session=session, delivery_boy_id=boy_id)
    if not delivery_boy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Delivery boy {boy_id} not found!",
        )

    return await update_delivery_boy(
        session=session,
        delivery_boy=delivery_boy,
        delivery_object=boy,
    )


@router.patch("/{boy_id}/", response_model=DeliveryBoyUpdatePartialSchema)
async def update_partial_boy(
        boy_id: int,
        boy: DeliveryBoyUpdatePartialSchema,
        session: AsyncSession = Depends(get_async_session),
) -> DeliveryBoy:
    delivery_boy = await get_delivery_boy(session=session, delivery_boy_id=boy_id)
    if not delivery_boy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Delivery boy {boy_id} not found!",
        )

    return await update_partial_delivery_boy(
        session=session,
        delivery_boy=delivery_boy,
        delivery_object=boy,
        partial=True
    )


@router.delete("/{boy_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_boy(
        boy_id: int,
        session: AsyncSession = Depends(get_async_session),
) -> None:
    delivery_boy = await get_delivery_boy(session=session, delivery_boy_id=boy_id)
    if not delivery_boy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Delivery boy {boy_id} not found!",
        )
    await delete_delivery_boy(
        session=session,
        delivery_boy=delivery_boy
    )
