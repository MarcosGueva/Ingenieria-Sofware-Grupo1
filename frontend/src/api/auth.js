// src/api/auth.js
import { api } from "./client";

/** Helpers de token */
export const TOKEN_KEY = "token";
export function saveToken(t) { localStorage.setItem(TOKEN_KEY, t); }
export function getToken() { return localStorage.getItem(TOKEN_KEY); }
export function logout() { localStorage.removeItem(TOKEN_KEY); }
export function isAuthenticated() { return Boolean(getToken()); }

/** Login */
export async function login({ email, password }) {
  const payload = {
    email: String(email || "").trim(),
    password: String(password || ""),
  };
  const data = await api.post("/auth/login", payload);
  if (data?.access_token) saveToken(data.access_token);
  return data; // { access_token, token_type }
}

/** Registro: el backend exige username, email, password */
export async function registerUser({ name, email, password }) {
  const payload = {
    username: String(name || "").trim(),
    email: String(email || "").trim(),
    password: String(password || ""),
  };
  return api.post("/auth/register", payload);
}
