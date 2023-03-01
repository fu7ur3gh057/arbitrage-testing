from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DealDTO(BaseModel):
    id: Optional[int] = None
    customer_id: int
    performer_id: int
    title: str
    description: str
    price: float
    currency: str
    deadline: Optional[datetime] = None
    type: str
    status: str
    room_id: Optional[int] = None
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True


class DealInputDTO(BaseModel):
    customer_id: int
    performer_id: int
    title: str
    description: str
    price: float
    currency: str
    deadline: Optional[datetime] = None


class DealConfirmDTO(BaseModel):
    deal_id: int
    room_id: int
