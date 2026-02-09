console.log("CARREGADO MEU NOBRE")
document.addEventListener("DOMContentLoaded", () => {
  $("btnLogin").addEventListener("click", login);
  $("btnRegister").addEventListener("click", register);
});

async function login() {
  clearAlert();
  const email = $("loginEmail").value.trim();
  const senha = $("loginSenha").value;

  if (!email || !senha) return showAlert("Login", "Preencha e-mail e senha.");
  if (!isEmailEscolar(email)) return showAlert("Login", "Use um e-mail @escolar.ifrn.edu.br.");

  try {
    await api("/api/auth/login", { method: "POST", body: { email, senha } });
    window.location.href = "/tarefas/disponiveis";
  } catch (e) {
    if (e.status === 401) showAlert("Login", "E-mail ou senha incorretos.");
    else showAlert("Login", extractServerMessage(e));
  }
}

async function register() {
  clearAlert();
  const nome = $("regNome").value.trim();
  const email = $("regEmail").value.trim();
  const senha = $("regSenha").value;

  if (!nome || !email || !senha) return showAlert("Cadastro", "Preencha nome, e-mail e senha.");
  if (!isEmailEscolar(email)) return showAlert("Cadastro", "O e-mail deve terminar com @escolar.ifrn.edu.br.");
  if (senha.length < 8) return showAlert("Cadastro", "A senha deve ter pelo menos 8 caracteres.");

  try {
    await api("/api/auth/register", { method: "POST", body: { nome, email, senha } });
    window.location.href = "/tarefas/disponiveis";
  } catch (e) {
    if (e.status === 409) showAlert("Cadastro", "E-mail já cadastrado. Faça login.");
    else showAlert("Cadastro", extractServerMessage(e));
  }
}
