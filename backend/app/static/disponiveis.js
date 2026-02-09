document.addEventListener("DOMContentLoaded", () => {
  $("btnRefreshDisponiveis").addEventListener("click", loadDisponiveis);
  loadDisponiveis();
});

function renderList(el, tarefas) {
  if (!Array.isArray(tarefas) || tarefas.length === 0) {
    el.innerHTML = `<div class="hint">Nenhuma tarefa disponível.</div>`;
    return;
  }

  el.innerHTML = tarefas.map(t => `
    <div class="item">
      <div class="itemTop">
        <div class="itemTitle">${t.titulo}</div>
        <div class="badge">${STATUS_LABEL[t.status] || t.status}</div>
      </div>
      <div class="itemDesc">${t.descricao}</div>
      <div class="itemMeta">
        <span class="badge">ID: ${t.id}</span> ·
        <span class="badge">Categoria: ${CATEGORIA_LABEL[t.categoria] || t.categoria}</span> ·
        <span class="badge">Prazo: ${t.prazo}</span>
      </div>
      <div class="itemActions">
        <button class="btn primary" onclick="acceptTask(${t.id})">Aceitar</button>
      </div>
    </div>
  `).join("");
}

async function loadDisponiveis(){
  clearAlert();
  try {
    const r = await api("/api/tarefas/disponiveis");
    renderList($("listaDisponiveis"), r.data);
  } catch {
    window.location.href = "/";
  }
}

window.acceptTask = async function(tarefaId){
  clearAlert();
  try {
    await api(`/api/tarefas/${tarefaId}/aceitar`, { method:"PATCH" });
    showAlert("Aceitar tarefa", "Tarefa aceita com sucesso.");
    await loadDisponiveis();
  } catch (e) {
    showAlert("Aceitar tarefa", extractServerMessage(e));
  }
}
