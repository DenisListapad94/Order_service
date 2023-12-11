from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class DeliveryBoy(Base):
    __tablename__ = "delivery_boy"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    age: Mapped[int]

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname}"



#todo
    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )

# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r


# with Session(engine) as session:
#     spongebob = DeliveryBoy(
#         name="spongebob",
#         fullname="Spongebob Squarepants",
#     )
#     sandy = DeliveryBoy(
#         name="sandy",
#         fullname="Sandy Cheeks",
#     )
#     patrick = DeliveryBoy(
#         name="patrick",
#         fullname="Patrick Star"
#     )
#
#     session.add_all([spongebob, sandy, patrick])
#
#     session.commit()

# with Session(engine) as session:
#     boys = session.query(DeliveryBoy.name,DeliveryBoy.fullname).all()
#     for boy in boys:
#          print(boy.name,boy.fullname)

# with Session(engine) as session:
#     boys = session.query(DeliveryBoy.name).filter((DeliveryBoy.name == "Sandy"))
#     for boy in boys:
#         print(boy.name,boy.surname)
#
#
#
# with Session(engine) as session:
#     waiters = session.query(DeliveryBoy).filter(DeliveryBoy.age>=10).order_by(-DeliveryBoy.age).limit(4).offset(2)
#     for waiter in waiters:
#         print(waiter.name,waiter.age)
#
# with Session(engine) as session:
#     waiter = session.query(DeliveryBoy).filter(DeliveryBoy.waiter_id==7).first()
#     session.delete(waiter)
#     session.commit()


# TODO group_by
# with Session(engine) as session:
#     # waiter_tables_count = session.query(TableReservation).join(Waiters).group_by(Waiters.waiter_id)
#     waiter_tables_count = session.query(TableReservation.table_id,
#                   func.count(Waiters.waiter_id)).group_by(Waiters.waiter_id).all()
#     for table in waiter_tables_count:
#         print(table)
