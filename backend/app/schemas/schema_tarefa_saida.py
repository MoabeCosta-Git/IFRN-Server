from .. import ma
from ..models.tarefa import Tarefa

class TarefaSaida(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tarefa

    