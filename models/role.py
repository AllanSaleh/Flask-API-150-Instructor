from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Role(Base):
    __tablename__ = "Roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(db.String(100), unique=True)

    ## GO TO THE CUSTOMER.PY FILE TO CREATE A RELATIONSHIP BETWEEN THE CUSTOMER AND ROLE TABLES