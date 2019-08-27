from marshmallow import Schema, fields
from .common import DateTimeMixinSchema


class UserSerializer(DateTimeMixinSchema, Schema):
    id = fields.Int()
    type = fields.Str()
    login = fields.Str()
    name = fields.Str()
    avatar_url = fields.Str()
