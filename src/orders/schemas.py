from typing import List

from pydantic import BaseModel, ConfigDict, PositiveInt

from .models import DeliveStatus


class DeliveryBoyBaseSchema(BaseModel):
    name: str
    fullname: str
    age: PositiveInt


class DeliveryBoyCreateSchema(DeliveryBoyBaseSchema):
    pass


class DeliveryBoyUpdateSchema(DeliveryBoyCreateSchema):
    pass


class DeliveryBoyUpdatePartialSchema(DeliveryBoyCreateSchema):
    name: str | None = None
    fullname: str | None = None
    age: PositiveInt | None = None


class DeliveryBoySchema(DeliveryBoyBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    id: PositiveInt


class OrderSchema(BaseModel):
    customer_id: PositiveInt | None = None
    delivery_boy_id: PositiveInt | None = None
    items: str
    delivery_status: DeliveStatus


class DeliveryBoyOrders(BaseModel):
    name: str
    order: List[OrderSchema]
