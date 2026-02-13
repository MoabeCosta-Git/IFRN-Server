from marshmallow import Schema, fields, validate, ValidationError
from app.extensions import ma
from app.models.usuario import Usuario

def validar_email(value):
    if not value.endswith("@escolar.ifrn.edu.br"):
        raise ValidationError("Domínio do e-mail inválido!")

class UsuarioEntrada(Schema):
    nome = fields.String(
        required=True,
        validate=validate.Length(
            min=1,
            max=100,
            error="O nome deve ter entre 1 e 100 caracteres."))
    
    email = fields.Email(
        required=True,
        validate=validar_email,
        error_messages={
        "invalid": "E-mail inválido."})

    senha = fields.String(
        required=True,
        validate=validate.Length(
            min=8,
            max=255,
            error="A senha deve ter no mínimo 8 caracteres."),
            load_only=True)
    
class UsuarioSaida(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        fields = ("id", "nome", "email", "admin")

class UsuarioUpdateSchema(Schema):
    nome = fields.String(
        required=True,
        validate=validate.Length(
            min=1,
            max=100,
            error="O nome deve ter entre 1 e 100 caracteres."))