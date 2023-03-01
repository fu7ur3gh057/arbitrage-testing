from typing import Union

from fastapi import APIRouter, Depends, HTTPException

from server.db.dao.deal_dao import DealDAO
from server.db.enums import DealStatus
from server.db.dao.chat_dao import RoomDAO
from server.db.models.deal_model import DealModel

from server.web.api.deals.schema import DealInputDTO, DealDTO

router = APIRouter()


async def get_deal_or_raise(deal_id: int, deal_dao: DealDAO) -> DealModel:
    deal = await deal_dao.get_deal_by_id(deal_id=deal_id)
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    else:
        return deal


def deal_is_created(deal: DealModel):
    if deal.status == DealStatus.CREATED:
        return True
    else:
        raise HTTPException(status_code=200, detail="Deal Status is not Created")


@router.get("/{deal_id}")
async def get_deal(deal_id: int, deal_dao: DealDAO = Depends()) -> DealDTO:
    deal = await get_deal_or_raise(deal_id=deal_id, deal_dao=deal_dao)
    return DealDTO(**deal.__dict__)


@router.post("/")
async def create_deal(data: DealInputDTO, deal_dao: DealDAO = Depends()) -> int:
    new_deal = await deal_dao.create_deal(data=data)
    if not new_deal:
        raise HTTPException(status_code=404, detail="User not found")
    return new_deal.id


@router.put("/{deal_id}/confirm")
async def confirm_deal(deal_id: int, deal_dao: DealDAO = Depends()) -> dict:
    deal = await get_deal_or_raise(deal_id=deal_id, deal_dao=deal_dao)
    deal_is_created(deal=deal)
    room_dao = RoomDAO()
    customer = await deal.customer
    performer = await deal.performer
    room = await room_dao.create_room(deal=deal, users=[customer, performer])
    await deal_dao.change_deal_status(deal=deal, status=DealStatus.IN_PROCESS)
    return {"deal_id": deal.id, "room_id": room.id}


@router.put("/{deal_id}/deny")
async def deny_deal(deal_id: int, deal_dao: DealDAO = Depends()) -> bool:
    deal = await get_deal_or_raise(deal_id=deal_id, deal_dao=deal_dao)
    deal_is_created(deal=deal)
    await deal_dao.change_deal_status(deal=deal, status=DealStatus.DENY_PERFORMER)
    return True
