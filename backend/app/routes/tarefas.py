from flask import Blueprint, request
from app.schemas.tarefa import TarefaEntrada,TarefaSaida, AtualizarPrestador
from app.services.tarefas import criar_tarefa, aceitar_tarefa
from app.models.tarefa import Tarefa
from flask_login import login_required, current_user

tarefa_bp = Blueprint("tarefas", __name__)

@tarefa_bp.post("/")
@login_required
def criar():
    data = TarefaEntrada().load(request.get_json() or {})
    tarefa = criar_tarefa(data, solicitante_id=current_user.id)
    return TarefaSaida().dump(tarefa),201

@tarefa_bp.patch("/<int:id>/aceitar")
@login_required
def aceitar(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)    
    tarefa = aceitar_tarefa(tarefa, usuario_id=current_user.id)
    return TarefaSaida().dump(tarefa)