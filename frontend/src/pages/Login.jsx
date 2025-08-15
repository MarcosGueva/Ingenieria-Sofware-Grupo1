import { useState, useMemo } from "react";
import { login as doLogin } from "../api/auth";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Login() {
  const nav = useNavigate();
  const { login } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPwd, setShowPwd] = useState(false);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");

  const formValid = useMemo(() => {
    const okEmail = /\S+@\S+\.\S+/.test(email);
    return okEmail && password.length >= 6;
  }, [email, password]);

  async function onSubmit(e) {
    e.preventDefault();
    setErr("");
    setLoading(true);
    try {
      // 👇 IMPORTANTE: pasar un objeto { email, password }
      await doLogin({ email, password });
      login();      // actualiza el contexto (guardas token en auth.js)
      nav("/");     // redirige (ajusta si tu ruta inicial es otra)
    } catch (e) {
      // Intenta mostrar mensajes de validación 422 de FastAPI
      const detail = e?.data?.detail;
      if (Array.isArray(detail) && detail.length) {
        const msgs = detail.map(d => {
          const campo = Array.isArray(d.loc) ? d.loc.at(-1) : "";
          return `${campo}: ${d.msg}`;
        }).join(" | ");
        setErr(msgs);
      } else {
        setErr(e.message || "Error al iniciar sesión");
      }
      console.error("Login error:", e.status, e.data);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="auth-wrap">
      <div className="auth-card">
        <h1 className="auth-title">Iniciar sesión</h1>

        <form onSubmit={onSubmit} className="auth-form" noValidate>
          <label className="auth-label" htmlFor="email">Email</label>
          <input
            id="email"
            name="email"
            className="auth-input"
            type="email"
            placeholder="tucorreo@dominio.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            autoComplete="email"
          />

          <label className="auth-label" htmlFor="password">Contraseña</label>
          <div className="auth-input-group">
            <input
              id="password"
              name="password"
              className="auth-input"
              type={showPwd ? "text" : "password"}
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              minLength={6}
              autoComplete="current-password"
            />
            <button
              type="button"
              className="auth-eye"
              aria-label={showPwd ? "Ocultar contraseña" : "Mostrar contraseña"}
              onClick={() => setShowPwd(s => !s)}
            >
              {showPwd ? "🙈" : "👁️"}
            </button>
          </div>

          {err && <p className="auth-error">{err}</p>}

          <button className="auth-btn" type="submit" disabled={!formValid || loading}>
            {loading ? "Entrando..." : "Entrar"}
          </button>
        </form>

        <p className="auth-foot">
          ¿No tienes cuenta? <Link to="/register">Regístrate</Link>
        </p>
      </div>
    </div>
  );
}
