from marshmallow import Schema, fields

class AtualizarPrestador(Schema):
    prestador_id = fields.Integer(required=True)