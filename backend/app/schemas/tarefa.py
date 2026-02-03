from marshmallow import Schema, fields, validate
from app.extensions import ma
from app.models.enums import Categoria
from app.utils.enum_utils import enum_values
from app.models.tarefa import Tarefa

class TarefaEntrada(Schema):
    titulo = fields.String(
        required=True,
        validate=validate.Length(
            min=10,
            max=100,
            error="O título deve ter entre 10 e 100 caracteres!"))
    
    descricao = fields.String(
        required=True,
        validate=validate.Length(
            min=20,
            max=255,
            error="A descrição deve ter entre 20 e 255 caracteres!"))
    
    categoria = fields.String(
        required=True,
        validate=validate.OneOf(enum_values(Categoria)))
    
    prazo = fields.Date(
        required=True,
        format="%d/%m/%Y",
        error_messages={
            "invalid": "Formato de data inválido. Use DD/MM/AAAA."
    })

class TarefaSaida(ma.SQLAlchemyAutoSchema):
    prazo = fields.Date(format="%d/%m/%Y")
    
    class Meta:
        model = Tarefa
        fields = (
            "id",
            "titulo",
            "descricao",
            "categoria",
            "status",
            "prazo",
            "campus",
            "solicitante_id",
            "prestador_id",
            "data_criacao")