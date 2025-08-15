const BASE_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

function authHeaders() {
  const token = localStorage.getItem("token");
  return token ? { Authorization: `Bearer ${token}` } : {};
}

async function request(path, { method = "GET", body, headers = {} } = {}) {
  const res = await fetch(`${BASE_URL}${path}`, {
    method,
    headers: {
      "Content-Type": "application/json",
      ...authHeaders(),
      ...headers,
    },
    body: body ? JSON.stringify(body) : undefined,
  });

  let data = null;
  try { data = await res.json(); } catch {}

  if (!res.ok) {
    throw new Error(data?.detail || `Error ${res.status}`);
  }
  return data;
}

export const api = {
  get: (p, o) => request(p, { method: "GET", ...o }),
  post: (p, b, o) => request(p, { method: "POST", body: b, ...o }),
};
