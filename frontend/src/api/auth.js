import { api } from "./client";

export async function login(email, password) {
  const data = await api.post("/auth/login", { email, password });
  localStorage.setItem("token", data.access_token);
  return data;
}

export async function registerUser(payload) {
  // payload: { name, email, password }
  return api.post("/auth/register", payload);
}

export function logout() {
  localStorage.removeItem("token");
}
export function isAuthenticated() {
  return Boolean(localStorage.getItem("token"));
}
