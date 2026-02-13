document.addEventListener("DOMContentLoaded", () => {
  $("btnRefreshSolicitadas").addEventListener("click", loadSolicitadas);
  $("btnRefreshPrestadas").addEventListener("click", loadPrestadas);
  $("filtroSolicitadas").addEventListener("change", loadSolicitadas);
  $("filtroPrestadas").addEventListener("change", loadPrestadas);

  // Carrega info do usuário para saber se é admin
  api("/api/usuarios/me").then(r => { window.me = r.data; loadSolicitadas(); loadPrestadas(); });
});

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
    // Botão para concluir tarefa prestada
    if (window.me && t.prestador_id === window.me.id && t.status !== "concluido") {
      actions += `<button class='btn primary' onclick='concluirTask(${t.id})'>Concluir</button>`;
    }
    return `
      <div class="item itemWide">
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
window.concluirTask = async function(tarefaId) {
  clearAlert();
  try {
    await api(`/api/tarefas/${tarefaId}`, { method: "PATCH", body: { status: "concluido" } });
    showAlert("Concluir tarefa", "Tarefa marcada como concluída.");
    await loadSolicitadas();
    if (typeof loadPrestadas === "function") await loadPrestadas();
  } catch (e) {
    showAlert("Concluir tarefa", extractServerMessage(e));
  }
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

async function loadSolicitadas(){
  clearAlert();
  try{
    const status = $("filtroSolicitadas").value;
    const qs = status ? `?status=${encodeURIComponent(status)}` : "";
    const r = await api(`/api/tarefas/minhas-solicitadas${qs}`);
    renderList($("listaSolicitadas"), r.data);
  }catch{
    window.location.href="/";
  }
}

async function loadPrestadas(){
  clearAlert();
  try{
    const status = $("filtroPrestadas").value;
    const qs = status ? `?status=${encodeURIComponent(status)}` : "";
    const r = await api(`/api/tarefas/minhas-prestadas${qs}`);
    renderList($("listaPrestadas"), r.data);
  }catch{
    window.location.href="/";
  }
}
