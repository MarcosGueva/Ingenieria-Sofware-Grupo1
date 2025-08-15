import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { registerUser } from "../api/auth";

export default function Register() {
  const nav = useNavigate();
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const [showPwd, setShowPwd] = useState(false);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");
  const [msg, setMsg] = useState("");

  function onChange(e) {
    const { name, value } = e.target;
    setForm((f) => ({ ...f, [name]: value }));
  }

  function valid() {
    return (
      form.name.trim().length >= 3 &&
      /\S+@\S+\.\S+/.test(form.email) &&
      form.password.length >= 6
    );
  }

  async function onSubmit(e) {
    e.preventDefault();
    setErr(""); setMsg(""); setLoading(true);

    try {
      // IMPORTANTE: el backend quiere username → mapeado inside registerUser
      await registerUser({
        name: form.name,
        email: form.email,
        password: form.password,
      });

      setMsg("¡Cuenta creada! Redirigiendo al login…");
      setTimeout(() => nav("/login"), 900);
    } catch (e) {
      // pinta mensajes 422 de FastAPI de forma legible
      const detail = e?.data?.detail;
      if (Array.isArray(detail) && detail.length) {
        const msgs = detail
          .map((d) => {
            const campo = Array.isArray(d.loc) ? d.loc.at(-1) : "";
            return `${campo}: ${d.msg}`;
          })
          .join(" | ");
        setErr(msgs);
      } else {
        setErr(e.message || "No se pudo registrar");
      }
      console.error("Register error:", e.status, e.data);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="auth-wrap">
      <section className="auth-card" style={{ width: "100%", maxWidth: 520 }}>
        <h1 className="auth-title">Crear cuenta</h1>

        <form className="auth-form" onSubmit={onSubmit} noValidate>
          <label className="auth-label" htmlFor="name">Nombre</label>
          <input
            id="name"
            name="name"
            className="auth-input"
            placeholder="Tu nombre"
            value={form.name}
            onChange={onChange}
            minLength={3}
            required
          />

          <label className="auth-label" htmlFor="email">Email</label>
          <input
            id="email"
            name="email"
            type="email"
            className="auth-input"
            placeholder="tucorreo@dominio.com"
            value={form.email}
            onChange={onChange}
            required
          />

          <label className="auth-label" htmlFor="password">Contraseña</label>
          <div className="auth-input-group">
            <input
              id="password"
              name="password"
              type={showPwd ? "text" : "password"}
              className="auth-input"
              placeholder="Mínimo 6 caracteres"
              value={form.password}
              onChange={onChange}
              minLength={6}
              required
            />
            <button
              type="button"
              className="auth-eye"
              aria-label={showPwd ? "Ocultar contraseña" : "Mostrar contraseña"}
              onClick={() => setShowPwd((v) => !v)}
            >
              {showPwd ? "🙈" : "👁️"}
            </button>
          </div>

          {err && <div className="auth-error">{err}</div>}
          {msg && <div style={{ color: "#9be37a", marginTop: 6 }}>{msg}</div>}

          <button className="auth-btn" disabled={!valid() || loading}>
            {loading ? "Creando..." : "Registrarme"}
          </button>

          <div className="auth-foot">
            ¿Ya tienes cuenta? <Link to="/login">Inicia sesión</Link>
          </div>
        </form>
      </section>
    </main>
  );
}
