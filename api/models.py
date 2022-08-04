from sqlalchemy import DECIMAL, Boolean, Column, Float, ForeignKey, Integer, String

from .database import Base


class Item(Base):
    __tablename__ = "items"

## DECIMAL(5,0) is a workaround to get a 5 digit integer
    id = Column(DECIMAL(5,0), primary_key=True, index=True, nullable=False, autoincrement=True)
    name = Column(String(30), nullable=False)
    weight = Column(DECIMAL(4,2), nullable=False)
    description = Column(String, index=True, nullable=True)

