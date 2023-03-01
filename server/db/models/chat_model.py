from typing import Union

from tortoise import Model, fields, ForeignKeyFieldInstance, ManyToManyFieldInstance


class RoomModel(Model):
    users: ManyToManyFieldInstance = fields.ManyToManyField(
        "models.UserModel", related_name="rooms"
    )
    deal: ForeignKeyFieldInstance = fields.OneToOneField(
        "models.DealModel", related_name="room"
    )
    created = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "room_model"


class MessageModel(Model):
    room: ForeignKeyFieldInstance = fields.ForeignKeyField(
        "models.RoomModel", related_name="messages"
    )
    sender: ForeignKeyFieldInstance = fields.ForeignKeyField(
        "models.UserModel", related_name="messages"
    )
    text = fields.TextField()
    created = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "message_model"
