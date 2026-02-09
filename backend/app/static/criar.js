document.addEventListener("DOMContentLoaded", () => {
  $("btnCriarTarefa").addEventListener("click", createTask);
  $("btnClearTask").addEventListener("click", clearTaskForm);
});

function clearTaskForm(){
  $("tTitulo").value = "";
  $("tDescricao").value = "";
  $("tCategoria").value = "preventiva";
  $("tPrazo").value = "";
}

function isValidBRDate(s) {
  if (!/^\d{2}\/\d{2}\/\d{4}$/.test(s)) return false;
  const [dd, mm, yyyy] = s.split("/").map(Number);
  if (mm < 1 || mm > 12) return false;
  if (dd < 1 || dd > 31) return false;
  if (yyyy < 2000 || yyyy > 2100) return false;
  return true;
}

async function createTask(){
  clearAlert();
  const titulo = $("tTitulo").value.trim();
  const descricao = $("tDescricao").value.trim();
  const categoria = $("tCategoria").value;
  const prazo = $("tPrazo").value.trim();

  if (titulo.length < 10) return showAlert("Criar tarefa", "Título com mínimo de 10 caracteres.");
  if (descricao.length < 20) return showAlert("Criar tarefa", "Descrição com mínimo de 20 caracteres.");
  if (!isValidBRDate(prazo)) return showAlert("Criar tarefa", "Prazo inválido. Use DD/MM/AAAA.");

  try {
    await api("/api/tarefas/", { method:"POST", body:{ titulo, descricao, categoria, prazo }});
    showAlert("Criar tarefa", "Tarefa criada com sucesso.");
    clearTaskForm();
  } catch (e) {
    if (e.status === 401) showAlert("Criar tarefa", "Faça login para criar tarefas.");
    else showAlert("Criar tarefa", extractServerMessage(e));
  }
}
