from typing import Union

from tortoise import Model, fields, ForeignKeyFieldInstance

from server.db.enums import Currency, DealType, DealStatus


class DealModel(Model):
    customer: ForeignKeyFieldInstance = fields.ForeignKeyField(
        "models.UserModel", related_name="customer_deals"
    )
    performer: ForeignKeyFieldInstance = fields.ForeignKeyField(
        "models.UserModel", related_name="performer_deals"
    )
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    price = fields.FloatField()
    currency = fields.CharEnumField(enum_type=Currency)
    deadline = fields.DatetimeField(null=True)
    type = fields.CharEnumField(enum_type=DealType)
    status = fields.CharEnumField(DealStatus)
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "deal_model"
