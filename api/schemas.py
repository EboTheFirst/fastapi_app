from typing import Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    weight: float
    description: Union[str, None] = None


class Item(ItemBase):
    id: int
    
    class Config:
        orm_mode = True