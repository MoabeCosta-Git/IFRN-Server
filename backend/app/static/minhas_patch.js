// ...existing code...
function renderList(el, tarefas) {
  if (!Array.isArray(tarefas) || tarefas.length === 0) {
    el.innerHTML = `<div class="hint">Nenhuma tarefa encontrada.</div>`;
    return;
  }
  el.innerHTML = tarefas.map(t => {
    let actions = "";
    if (window.me && (window.me.admin || t.solicitante_id === window.me.id)) {
      actions += `<button class='btn danger' onclick='deleteTask(${t.id})'>Excluir</button>`;
      actions += `<button class='btn' onclick='editTask(${t.id})'>Editar</button>`;
    }
    return `
      <div class="item">
        <div class="itemTop">
          <div class="itemTitle">${t.titulo}</div>
          <div class="badge">${STATUS_LABEL[t.status] || t.status}</div>
        </div>
        <div class="itemDesc">${t.descricao}</div>
        <div class="itemMeta">
          <span class="badge">Categoria: ${CATEGORIA_LABEL[t.categoria] || t.categoria}</span> ·
          <span class="badge">Prazo: ${t.prazo}</span> ·
          <span class="badge">Campus: ${t.campus}</span>
        </div>
        <div class="itemActions">${actions}</div>
      </div>
    `;
  }).join("");
}

window.deleteTask = async function(tarefaId) {
  if (!confirm("Tem certeza que deseja excluir esta tarefa?")) return;
  clearAlert();
  try {
    await api(`/api/tarefas/${tarefaId}`, { method: "DELETE" });
    showAlert("Excluir tarefa", "Tarefa excluída com sucesso.");
    await loadSolicitadas();
    if (typeof loadPrestadas === "function") await loadPrestadas();
  } catch (e) {
    showAlert("Excluir tarefa", extractServerMessage(e));
  }
}

window.editTask = function(tarefaId) {
  window.location.href = `/tarefas/editar/${tarefaId}`;
}
// ...existing code...
document.addEventListener("DOMContentLoaded", () => {
  $("btnRefreshSolicitadas").addEventListener("click", loadSolicitadas);
  $("btnRefreshPrestadas").addEventListener("click", loadPrestadas);
  $("filtroSolicitadas").addEventListener("change", loadSolicitadas);
  $("filtroPrestadas").addEventListener("change", loadPrestadas);

  // Carrega info do usuário para saber se é admin
  api("/api/usuarios/me").then(r => { window.me = r.data; loadSolicitadas(); loadPrestadas(); });
});
// ...existing code...
