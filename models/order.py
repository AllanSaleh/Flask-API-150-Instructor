from typing import List
import datetime
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from models.orderProduct import order_product

class Order(Base):
    __tablename__ = 'Orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.date] = mapped_column(db.Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('Customers.id'))
    # Many-To-One: Order and Customer     
    customer: Mapped["Customer"] = db.relationship(back_populates="orders")
    # Many-to-Many: Products and Orders with no back_populates
    products: Mapped[List["Product"]] = db.relationship(secondary=order_product) 

    # products: Mapped[List["Product"]] = db.relationship(secondary=order_product, lazy='noload') 

    ## lazy='noload' means that the products attribute will not be loaded when the Order object is queried from the database. This is useful when we don't need the products attribute and we want to improve performance by not loading it. We can load the products attribute later when we need it by using the db.session.load() method.
    ## eager loading is the opposite of lazy loading. It means that the products attribute will be loaded when the Order object is queried from the database. This is useful when we need the products attribute and we want to avoid additional queries to load it. We can use eager loading by setting lazy='joined' or lazy='select' in the db.relationship() function.