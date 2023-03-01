from typing import Optional, Union, List

from server.db.models.deal_model import DealModel
from server.db.models.user_model import UserModel
from server.web.api.users.schema import UserInputDTO


class UserDAO:
    async def create_user(self, name: str, external_id: int) -> UserModel:
        return await UserModel.create(name=name, external_id=external_id)

    async def get_user_by_id(self, user_id: int) -> Union[UserModel, None]:
        return await UserModel.get_or_none(id=user_id)

    async def get_user_deals(self, user_id: int) -> Union[List[DealModel], None]:
        user = await self.get_user_by_id(user_id=user_id)
        if not user:
            return None
        deals = await user.customer_deals + await user.performer_deals
        return deals

    async def delete_user_by_id(self, user_id: int) -> bool:
        pass
