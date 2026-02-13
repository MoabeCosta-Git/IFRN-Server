document.addEventListener("DOMContentLoaded", async () => {
  const tarefaId = window.location.pathname.split("/").pop();
  const form = document.getElementById("formEditarTarefa");
  const titulo = document.getElementById("titulo");
  const descricao = document.getElementById("descricao");
  const categoria = document.getElementById("categoria");
  const prazo = document.getElementById("prazo");

  // Carregar dados da tarefa
  try {
    const r = await api(`/api/tarefas/${tarefaId}`);
    const t = r.data;
    titulo.value = t.titulo;
    descricao.value = t.descricao;
    categoria.value = t.categoria;
    prazo.value = t.prazo;
  } catch (e) {
    showAlert("Editar tarefa", extractServerMessage(e));
  }

  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    clearAlert();
    try {
      await api(`/api/tarefas/${tarefaId}`, {
        method: "PATCH",
        body: {
          titulo: titulo.value,
          descricao: descricao.value,
          categoria: categoria.value,
          prazo: prazo.value
        }
      });
      showAlert("Editar tarefa", "Tarefa atualizada com sucesso.");
      setTimeout(() => window.location.href = "/tarefas/minhas", 1200);
    } catch (e) {
      showAlert("Editar tarefa", extractServerMessage(e));
    }
  });
});
