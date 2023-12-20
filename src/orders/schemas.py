from pydantic import BaseModel, ConfigDict, PositiveInt


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
