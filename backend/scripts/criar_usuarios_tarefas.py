import requests

BASE_URL = "http://localhost:5000/api"


usuarios = [
    {"nome": "Usuario B", "email": "usuariob@escolar.ifrn.edu.br", "senha": "senha1234"},
    {"nome": "Usuario C", "email": "usuarioc@escolar.ifrn.edu.br", "senha": "senha1234"},
    {"nome": "Usuario D", "email": "usuariod@escolar.ifrn.edu.br", "senha": "senha1234"},
    {"nome": "Usuario E", "email": "usuarioe@escolar.ifrn.edu.br", "senha": "senha1234"},
    {"nome": "Usuario F", "email": "usuariof@escolar.ifrn.edu.br", "senha": "senha1234"},
]

# Categorias válidas: 'preventiva', 'defeito'
categorias = ["preventiva", "defeito"]

def gerar_tarefas():
    tarefas = []
    for idx, u in enumerate(usuarios):
        for j in range(2):
            cat = categorias[(idx + j) % len(categorias)]
            tarefas.append({
                "titulo": f"Tarefa {j+1} de {u['nome']}",
                "descricao": f"Descrição detalhada da tarefa {j+1} do {u['nome']} para testes.",
                "categoria": cat,
                "prazo": "31/12/2026"
            })
    return tarefas

tarefas = gerar_tarefas()

def criar_usuario(usuario):
    r = requests.post(f"{BASE_URL}/auth/register", json=usuario)
    r.raise_for_status()
    print(f"Usuário criado: {usuario['email']}")
    return r.cookies


def criar_tarefa(tarefa, cookies):
    r = requests.post(f"{BASE_URL}/tarefas/", json=tarefa, cookies=cookies)
    try:
        r.raise_for_status()
        print(f"Tarefa criada: {tarefa['titulo']}")
    except Exception:
        print(f"Erro ao criar tarefa: {tarefa['titulo']} - {r.text}")

if __name__ == "__main__":
    for idx, usuario in enumerate(usuarios):
        cookies = criar_usuario(usuario)
        for t in tarefas[idx*2:idx*2+2]:
            criar_tarefa(t, cookies)
