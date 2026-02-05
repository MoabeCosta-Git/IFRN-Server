from flask import Blueprint, request, jsonify
from app.schemas.tarefa import TarefaEntrada,TarefaSaida
from app.services.tarefas import criar_tarefa, aceitar_tarefa
from app.models.tarefa import Tarefa
from flask_login import login_required, current_user
from app.utils.enum_utils import parse_status

tarefa_bp = Blueprint("tarefas", __name__)

tarefa_saida = TarefaSaida()
tarefas_saida = TarefaSaida(many=True)

@tarefa_bp.post("/")
@login_required
def criar():
    data = TarefaEntrada().load(request.get_json() or {})
    tarefa = criar_tarefa(data, solicitante_id=current_user.id)
    return jsonify(tarefa_saida.dump(tarefa),201)

@tarefa_bp.patch("/<int:tarefa_id>/aceitar")
@login_required
def aceitar(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)    
    tarefa = aceitar_tarefa(tarefa, usuario_id=current_user.id)
    return jsonify(tarefa_saida.dump(tarefa))

@tarefa_bp.get("/minhas-solicitadas")
@login_required
def minhas_solicitadas():
    status_url = request.args.get("status")
    query = Tarefa.query.filter_by(solicitante_id=current_user.id)

    status = None
    if status_url:
        status = parse_status(status_url)
    if status:
        query = query.filter_by(status=status)

    tarefas = query.order_by(Tarefa.id.desc()).all()
    return jsonify(tarefas_saida.dump(tarefas)), 200

@tarefa_bp.get("/minhas-prestadas")
@login_required
def minhas_prestadas():
    status_url = request.args.get("status")
    query = Tarefa.query.filter_by(prestador_id=current_user.id)

    status = None
    if status_url:
        status = parse_status(status_url)
    if status:
        query = query.filter_by(status=status)

    tarefas = query.order_by(Tarefa.id.desc()).all()
    return jsonify(tarefas_saida.dump(tarefas)), 200