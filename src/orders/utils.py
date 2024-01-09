from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import DeliveryBoy
from .service import get_delivery_boy


async def get_delivery_boy_by_id(
        boy_id: int,
        session: AsyncSession = Depends(get_async_session)
) -> DeliveryBoy:
    delivery_boy = await get_delivery_boy(session=session, delivery_boy_id=boy_id)
    if not delivery_boy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Delivery boy {boy_id} not found!",
        )
    return delivery_boy
