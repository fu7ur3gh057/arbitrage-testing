from datetime import datetime
from typing import Union, Optional

from server.db.enums import DealType, DealStatus
from server.db.models.deal_model import DealModel
from server.db.models.user_model import UserModel
from server.web.api.deals.schema import DealInputDTO


class DealDAO:
    async def create_deal(self, data: DealInputDTO) -> Union[DealModel, None]:
        from server.db.dao.user_dao import UserDAO

        user_dao = UserDAO()
        customer = await user_dao.get_user_by_id(user_id=data.customer_id)
        performer = await user_dao.get_user_by_id(user_id=data.performer_id)
        if not customer or not performer:
            return None
        return await DealModel.create(
            customer=customer,
            performer=performer,
            title=data.title,
            description=data.description,
            price=data.price,
            currency=data.currency,
            deadline=None,
            type=DealType.REGULAR,
            status=DealStatus.CREATED,
        )

    async def get_deal_by_id(self, deal_id: int) -> Union[DealModel, None]:
        return await DealModel.get_or_none(id=deal_id)

    async def change_deal_status(self, deal: DealModel, status: str) -> DealModel:
        deal = await self.get_deal_by_id(deal_id=deal.id)
        deal.status = status
        await deal.save()
        return deal

    async def delete_deal_by_id(self, deal_id: int) -> bool:
        pass
