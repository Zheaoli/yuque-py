from marshmallow import Schema, fields
from .user_serializer import UserSerializer
from .common import DateTimeMixinSchema


class BookSerializer(Schema, DateTimeMixinSchema):
    id = fields.Int()
    type = fields.Str()
    slug = fields.Str()
    name = fields.Str()
    namespace = fields.Str()
    user_id = fields.Str()
    user = fields.Nested(UserSerializer)
    description = fields.Str()
    creator_id = fields.Int()
    public = fields.Int()
    likes_count = fields.Int()
    watches_count = fields.Int()
