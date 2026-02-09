document.addEventListener("DOMContentLoaded", () => {
  $("btnRefreshSolicitadas").addEventListener("click", loadSolicitadas);
  $("btnRefreshPrestadas").addEventListener("click", loadPrestadas);
  $("filtroSolicitadas").addEventListener("change", loadSolicitadas);
  $("filtroPrestadas").addEventListener("change", loadPrestadas);

  loadSolicitadas();
  loadPrestadas();
});

function renderList(el, tarefas) {
  if (!Array.isArray(tarefas) || tarefas.length === 0) {
    el.innerHTML = `<div class="hint">Nenhuma tarefa encontrada.</div>`;
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
        <span class="badge">Categoria: ${CATEGORIA_LABEL[t.categoria] || t.categoria}</span> ·
        <span class="badge">Prazo: ${t.prazo}</span> ·
        <span class="badge">Campus: ${t.campus}</span>
      </div>
    </div>
  `).join("");
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
