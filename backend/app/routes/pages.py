from flask import Blueprint, render_template
from flask_login import login_required

pages_bp = Blueprint("pages", __name__)

@pages_bp.get("/")
def login():
    return render_template("login.html")

@pages_bp.get("/usuario")
@login_required
def usuario():
    return render_template("usuario.html")

@pages_bp.get("/tarefas/criar")
@login_required
def criar_tarefa():
    return render_template("criar_tarefa.html")

@pages_bp.get("/tarefas/disponiveis")
@login_required
def disponiveis():
    return render_template("disponiveis.html")

@pages_bp.get("/tarefas/minhas")
@login_required
def minhas():
    return render_template("minhas_tarefas.html")

@pages_bp.get("/tarefas/editar/<int:tarefa_id>")
def editar_tarefa(tarefa_id):
    return render_template("editar_tarefa.html", tarefa_id=tarefa_id)
