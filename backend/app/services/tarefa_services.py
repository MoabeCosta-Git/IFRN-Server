from ..extensions import db
from ..models.tarefa import Tarefa
from ..models.enums import StatusTarefa

def criar_tarefa(data, solicitante_id):
    tarefa = Tarefa(
        **data,
        solicitante_id=solicitante_id,
        status=StatusTarefa.pendente
    )
    db.session.add(tarefa)
    db.session.commit()
    
    return tarefa

def aceitar_tarefa(tarefa, prestador_id):
    if tarefa.prestador_id:
        raise ValueError("Tarefa já aceita")

    tarefa.prestador_id = prestador_id
    tarefa.status = StatusTarefa.em_andamento
    db.session.commit()

    return tarefa

