from typing import List

from server.db.models.chat_model import RoomModel
from server.db.models.deal_model import DealModel
from server.db.models.user_model import UserModel


class RoomDAO:
    async def create_room(self, deal: DealModel, users: list[UserModel]) -> RoomModel:
        room = await RoomModel.create(deal=deal)
        for i in users:
            print(i.name)
        await room.users.add(*users)
        await room.save()
        return room


class MessageDAO:
    async def create_message(self):
        pass
