const BASE_URL = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";

function authHeaders() {
  const t = localStorage.getItem("token");
  return t ? { Authorization: `Bearer ${t}` } : {};
}

async function request(path, { method = "GET", body, headers = {} } = {}) {
  const res = await fetch(`${BASE_URL}${path}`, {
    method,
    headers: { "Content-Type": "application/json", ...authHeaders(), ...headers },
    body: body ? JSON.stringify(body) : undefined,
  });

  let data = null;
  try { data = await res.json(); } catch {}

  if (!res.ok) {
    let message = `Error ${res.status}`;
    const detail = data?.detail ?? data?.message ?? data?.error;

    if (typeof detail === "string") message = detail;
    else if (Array.isArray(detail))
      message = detail.map(d => d.msg || d?.loc?.join(".")).join(", ");

    const err = new Error(message);
    err.status = res.status;
    err.data = data;
    throw err;
  }
  return data;
}

export const api = {
  get:  (p, o)    => request(p, { method: "GET",  ...o }),
  post: (p, b, o) => request(p, { method: "POST", body: b, ...o }),
};
