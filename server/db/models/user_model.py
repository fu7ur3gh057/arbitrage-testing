from tortoise import Model, fields


class UserModel(Model):
    name = fields.CharField(max_length=255)
    external_id = fields.IntField(null=True)
    is_arbitrage = fields.BooleanField(default=False)
    created = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "user_model"

    def __str__(self):
        return f"{self.id}"
