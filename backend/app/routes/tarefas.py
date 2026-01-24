from flask import Blueprint, request
from app.schemas.tarefa_schema import TarefaEntrada,TarefaSaida, AtualizarPrestador
from app.services.tarefa_services import criar_tarefa, aceitar_tarefa
from app.models.tarefa import Tarefa

tarefa_bp = Blueprint("tarefas", __name__)

@tarefa_bp.post("/")
def criar():
    data = TarefaEntrada().load(request.json)
    tarefa = criar_tarefa(data, solicitante_id=1)# depois vem auth
    return TarefaSaida().dump(tarefa),201

@tarefa_bp.patch("/<int:id>/aceitar")
def aceitar(id):
    data = AtualizarPrestador().load(request.json)
    tarefa = Tarefa.query.get_or_404(id)
    tarefa = aceitar_tarefa(tarefa, data["prestador_id"])
    return TarefaSaida().dump(tarefa)