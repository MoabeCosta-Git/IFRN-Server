const $ = (id) => document.getElementById(id);

const STATUS_LABEL = {
  pendente: "Pendente",
  em_andamento: "Em andamento",
  concluido: "Concluído",
};

const CATEGORIA_LABEL = {
  preventiva: "Manutenção preventiva",
  defeito: "Defeito/Mal funcionamento",
};

const logEl = $("log");
function log(msg, obj = null) {
  if (!logEl) return;
  const line = `[${new Date().toLocaleTimeString()}] ${msg}`;
  logEl.textContent = line + (obj ? `\n${JSON.stringify(obj, null, 2)}\n\n` : `\n`) + logEl.textContent;
}
function clearLogs(){ if (logEl) logEl.textContent=""; }

function showAlert(title, message) {
  $("alertTitle").textContent = title || "Aviso";
  $("alertMsg").textContent = message || "";
  $("alertBox").classList.remove("hidden");
}
function clearAlert() {
  $("alertBox").classList.add("hidden");
  $("alertTitle").textContent = "Aviso";
  $("alertMsg").textContent = "";
}

// converte erro do backend para uma mensagem pequena
function extractServerMessage(e) {
  const data = e?.data;

  if (data && typeof data === "object") {
    if (data.erro) return String(data.erro);
    const keys = Object.keys(data);
    if (keys.length) {
      const k = keys[0];
      const v = data[k];
      if (Array.isArray(v) && v.length) return String(v[0]);
      return `${k}: ${String(v)}`;
    }
    return "Erro na requisição.";
  }

  if (typeof data === "string") {
    const s = data.trim();
    if (s.startsWith("<!doctype") || s.startsWith("<html") || s.includes("<title>")) {
      const m = s.match(/<title>(.*?)<\/title>/i);
      if (m && m[1]) return "Erro no servidor.";
      return "Erro no servidor.";
    }
    return s.slice(0, 280);
  }

  return "Ocorreu um erro inesperado.";
}

function isEmailEscolar(email) {
  return typeof email === "string" && email.trim().toLowerCase().endsWith("@escolar.ifrn.edu.br");
}

async function api(path, { method = "GET", body = null } = {}) {
  const opts = {
    method,
    credentials: "include",
    headers: { "Content-Type": "application/json" },
  };
  if (body) opts.body = JSON.stringify(body);

  const res = await fetch(path, opts);
  const contentType = res.headers.get("content-type") || "";
  const data = contentType.includes("application/json") ? await res.json() : await res.text();

  if (!res.ok) {
    const err = new Error("API error");
    err.status = res.status;
    err.data = data;
    throw err;
  }
  return { status: res.status, data };
}

async function refreshTopUser() {
  try {
    const r = await api("/api/usuarios/me");
    const me = r.data;

    if (!me || typeof me !== "object" || !me.email) {
      throw new Error("not-logged");
    }

    if ($("whoami")) $("whoami").textContent = `${me.nome} (${me.email})`;
    if ($("btnLogout")) $("btnLogout").classList.remove("hidden");
    return me;
  } catch {
    if ($("whoami")) $("whoami").textContent = "Deslogado";
    if ($("btnLogout")) $("btnLogout").classList.add("hidden");
    return null;
  }
}

// eventos comuns
document.addEventListener("DOMContentLoaded", async () => {
  if ($("btnCloseAlert")) $("btnCloseAlert").addEventListener("click", clearAlert);
  if ($("btnClearLogs")) $("btnClearLogs").addEventListener("click", clearLogs);

  await refreshTopUser();

  if ($("btnLogout")) {
    $("btnLogout").addEventListener("click", async () => {
      clearAlert();
      try {
        await api("/api/auth/logout", { method: "POST" });
        window.location.href = "/";
      } catch (e) {
        showAlert("Sessão", extractServerMessage(e));
      }
    });
  }
});
