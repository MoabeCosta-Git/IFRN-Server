from marshmallow import Schema, fields

class LoginSchema(Schema):
    email = fields.Email(required=True)
    senha = fields.String(required=True, load_only=True)