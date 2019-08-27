from marshmallow import fields, Schema


class DateTimeMixinSchema:
    created_at = fields.DateTime("%Y-%m-%dT%H:%M:%S.%fZ")
    updated_at = fields.DateTime("%Y-%m-%dT%H:%M:%S.%fZ")
