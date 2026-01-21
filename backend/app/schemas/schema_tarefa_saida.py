from .. import ma
from ..models.tarefa import Tarefa

class TarefaSaida(ma.SQLAlchemyAutoSchema):
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
            "data_criacao"
        )

    