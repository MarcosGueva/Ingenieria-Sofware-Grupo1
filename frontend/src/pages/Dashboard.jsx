import { useEffect, useState } from "react";
import { logout } from "../api/auth";
import { useAuth } from "../context/AuthContext";

export default function Dashboard() {
  const { logout: ctxLogout } = useAuth();
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");
  const [totSocios, setTotSocios] = useState(null);

  async function refresh() {
    setErr("");
    setLoading(true);
    try {
      // TODO: aquí iría tu fetch real, por ahora simulo:
      await new Promise(r => setTimeout(r, 400));
      setTotSocios(0); // reemplaza con el valor real
    } catch (e) {
      setErr("No se pudo cargar la información");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => { refresh(); }, []);

  function doLogout() {
    logout();
    ctxLogout();
    window.location.href = "/login";
  }

  return (
    <div className="container">
      <div className="dash__head">
        <h1 className="dash__title">Panel</h1>
        <div className="btn-row">
          <button className="btn btn--brand" onClick={refresh} disabled={loading}>
            {loading ? "Actualizando…" : "Actualizar"}
          </button>
          <button className="btn btn--danger" onClick={doLogout}>Cerrar sesión</button>
        </div>
      </div>

      {err && <p className="muted" style={{color:"#ff8585"}}>{err}</p>}

      <section className="cards">
        <article className="card">
          <h3 className="card__title">Socios</h3>
          <div className="card__metric">{totSocios ?? "—"}</div>
          <span className="card__hint muted">Total registrados</span>
        </article>

        <article className="card">
          <h3 className="card__title">Ahorros (hoy)</h3>
          <div className="card__metric">—</div>
          <span className="card__hint muted">Próximamente</span>
        </article>

        <article className="card" style={{gridColumn: "1 / -1"}}>
          <h3 className="card__title">Créditos pendientes</h3>
          <div className="card__metric">—</div>
          <span className="card__hint muted">Próximamente</span>
        </article>
      </section>

      <h2 className="section-title">Acciones rápidas</h2>
      <section className="quick">
        <a className="link-card" href="#">
          <span className="link-card__title">Gestionar socios</span>
          <span className="link-card__sub">Ver, crear y editar</span>
        </a>

        <a className="link-card" href="#">
          <span className="link-card__title">Ahorros</span>
          <span className="link-card__sub">Depósitos y retiros</span>
        </a>

        <a className="link-card" href="#">
          <span className="link-card__title">Créditos</span>
          <span className="link-card__sub">Solicitudes y aprobación</span>
        </a>
      </section>
    </div>
  );
}
