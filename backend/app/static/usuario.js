document.addEventListener("DOMContentLoaded", async () => {
  await loadMe();
  $("btnRefreshMe").addEventListener("click", loadMe);
  $("btnAtualizarNome").addEventListener("click", updateName);
});

async function loadMe() {
  clearAlert();
  try {
    const r = await api("/api/usuarios/me");
    const me = r.data;
    $("meId").textContent = me.id ?? "-";
    $("meNome").textContent = me.nome ?? "-";
    $("meEmail").textContent = me.email ?? "-";
  } catch {
    window.location.href = "/";
  }
}

async function updateName() {
  clearAlert();
  const nome = $("novoNome").value.trim();
  if (!nome) return showAlert("Usuário", "Digite um nome para atualizar.");

  try {
    await api("/api/usuarios/me", { method: "PATCH", body: { nome } });
    $("novoNome").value = "";
    showAlert("Usuário", "Nome atualizado com sucesso.");
    await loadMe();
  } catch (e) {
    showAlert("Usuário", extractServerMessage(e));
  }
}
