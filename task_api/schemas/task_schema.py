
from marshmallow import Schema, fields, validate, validates_schema

class TaskCreateSchema(Schema):
    title = fields.String(required=True, validate=[validate.Length(min=1), validate.Length(max=200)])
    done = fields.Boolean(required=True)

class TaskUpdateSchema(Schema):
    title = fields.String(required=False, validate=[validate.Length(min=1), validate.Length(max=200)])
    done = fields.Boolean(required=False)

    @validates_schema
    def validate_at_least_one(self, data, **kwargs):
        if not data:
            raise validate.ValidationError("At least one field (title or done) must be provided.")