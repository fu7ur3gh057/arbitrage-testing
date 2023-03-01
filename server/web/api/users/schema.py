from typing import Optional, List

from pydantic import BaseModel

from server.web.api.deals.schema import DealDTO


class UserDTO(BaseModel):
    id: int
    name: str
    external_id: Optional[int] = None
    deal_count: int


class UserInputDTO(BaseModel):
    name: str
    external_id: Optional[int] = None


class UserDealsDTO(BaseModel):
    deal_list: List[DealDTO]

    class Config:
        arbitrary_types_allowed = True
