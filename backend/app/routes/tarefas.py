from flask import Blueprint, request, jsonify, abort
from app.schemas.tarefa import TarefaEntrada, TarefaSaida
from app.services.tarefas import criar_tarefa, aceitar_tarefa
from app.models.tarefa import Tarefa
from flask_login import login_required, current_user
from app.utils.enum_utils import parse_status
from app.models.enums import StatusTarefa
from app.extensions import db

tarefa_bp = Blueprint("tarefas", __name__, url_prefix="/api/tarefas")

tarefa_saida = TarefaSaida()
tarefas_saida = TarefaSaida(many=True)

def can_modify_tarefa(tarefa):
    return current_user.is_authenticated and (current_user.is_admin() or tarefa.solicitante_id == current_user.id)
@tarefa_bp.delete("/<int:tarefa_id>")
@login_required
def deletar_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    if not can_modify_tarefa(tarefa):
        abort(403, description="Sem permissão para excluir esta tarefa.")
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({"mensagem": "Tarefa excluída com sucesso."}), 200

@tarefa_bp.patch("/<int:tarefa_id>")
@login_required
def atualizar_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    if not can_modify_tarefa(tarefa):
        abort(403, description="Sem permissão para atualizar esta tarefa.")
    data = request.get_json() or {}
    # Atualiza apenas campos permitidos
    from datetime import datetime
    for campo in ["titulo", "descricao", "categoria", "prazo", "campus", "status"]:
        if campo in data:
            if campo == "prazo" and isinstance(data["prazo"], str):
                try:
                    # Espera formato DD/MM/AAAA
                    data_prazo = datetime.strptime(data["prazo"], "%d/%m/%Y")
                    setattr(tarefa, "prazo", data_prazo)
                except Exception:
                    continue
            else:
                setattr(tarefa, campo, data[campo])
    db.session.commit()
    return jsonify(tarefa_saida.dump(tarefa)), 200

@tarefa_bp.get("/todas")
@login_required
def todas_tarefas():
    if not current_user.is_admin():
        return jsonify({"erro": "Apenas administradores podem acessar esta rota."}), 403
    status_url = request.args.get("status")
    query = Tarefa.query
    status = None
    if status_url:
        status = parse_status(status_url)
    if status:
        query = query.filter_by(status=status)
    tarefas = query.order_by(Tarefa.id.desc()).all()
    return jsonify(tarefas_saida.dump(tarefas)), 200

@tarefa_bp.get("/disponiveis")
@login_required
def disponiveis():
    query = Tarefa.query.filter(
        Tarefa.status == StatusTarefa.pendente,
        Tarefa.prestador_id.is_(None),
        Tarefa.solicitante_id != current_user.id
    ).order_by(Tarefa.id.desc())

    tarefas = query.all()
    return jsonify(tarefas_saida.dump(tarefas)), 200

@tarefa_bp.post("/")
@login_required
def criar():
    data = TarefaEntrada().load(request.get_json() or {})
    tarefa = criar_tarefa(data, usuario_id=current_user.id)
    return jsonify(tarefa_saida.dump(tarefa)),201

@tarefa_bp.patch("/<int:tarefa_id>/aceitar")
@login_required
def aceitar(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)    
    tarefa = aceitar_tarefa(tarefa, usuario_id=current_user.id)
    return jsonify(tarefa_saida.dump(tarefa)), 200

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