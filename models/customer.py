from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class Customer(Base):
    __tablename__ = 'Customers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(db.String(20), nullable=False)
    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
     # One-to-Many: Customer and Order
    orders: Mapped[List["Order"]] = db.relationship(back_populates="customer")

    ## In MySQL, we would see the table Customers with the columns id, name, email, phone, username, and password. We wouldn't see the orders column because it's a relationship, not a column.
    ## Any Customer object that we query from the database will have an orders attribute that contains a list of Order objects associated with that Customer object.
    ## I can look at the orders attribute of a Customer object and that will point me to the Order objects associated with that Customer object.
    ## I don't to do any joins or queries to get the Order objects associated with a Customer object. I can just look at the orders attribute of the Customer object.
    ## This is the power of SQLAlchemy and the ORM. It allows me to easily navigate relationships between tables in a database.
    ## I need to deserialize the orders attribute of a Customer object to JSON so that I can return it to the frontend user. I can do this by creating a schema for the Order object and using the ma.Nested() field in the Customer schema.
    ## Our Schemas are set up to only show the table columns and not the relationships. We need to add the relationships to the schemas so that we can see the relationships in the JSON response.