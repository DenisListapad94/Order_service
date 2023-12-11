from pydantic import BaseModel, PositiveInt


class DeliveryBoySchema(BaseModel):
    id: PositiveInt
    name: str
    fullname: str
    age: PositiveInt
