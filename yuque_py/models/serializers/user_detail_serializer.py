from marshmallow import Schema, fields


class UserDetailSerializer(Schema):
    id = fields.Int()
    space_id = fields.Int()
    account_id = fields.Int()
    type = fields.Str()
    login = fields.Str()
    name = fields.Str()
    owner_id = fields.Int()
    avatar_url = fields.Str()
    books_count = fields.Int()
    public_books_count = fields.Int()
    members_count = fields.Int()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
