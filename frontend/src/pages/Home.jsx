import { Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

export default function Home() {
  const nav = useNavigate();
  const [logged, setLogged] = useState(false);

  useEffect(() => {
    // Si ya hay token, mostramos CTA a / (dashboard)
    setLogged(Boolean(localStorage.getItem("token")));
  }, []);

  return (
    <div className="container home">
      <section className="home-hero">
        {/* Columna izquierda: texto */}
        <div className="home-hero__text">
          <h1 className="home-title">
            Caja de Ahorros <span className="pill">v1</span>
          </h1>
          <p className="home-subtitle">
            Administra socios, depósitos, retiros y créditos desde una interfaz
            moderna y segura. Con reportes y auditoría listos para usar.
          </p>

          <div className="home-actions">
            {logged ? (
              <>
                <Link className="btn btn--brand" to="/">
                  Ir al panel
                </Link>
                <button className="btn" onClick={() => nav("/register")}>
                  Invitar / Registrar socio
                </button>
              </>
            ) : (
              <>
                <Link className="btn btn--brand" to="/login">
                  Iniciar sesión
                </Link>
                <Link className="btn" to="/register">
                  Crear cuenta
                </Link>
              </>
            )}
          </div>

          <ul className="home-bullets">
            <li>✔️ Depósitos y retiros</li>
            <li>✔️ Créditos y aprobaciones</li>
            <li>✔️ Reportes descargables</li>
            <li>✔️ Auditoría de acciones</li>
          </ul>
        </div>

        {/* Columna derecha: “tarjeta” ilustrativa */}
        <aside className="home-hero__card">
          <div className="home-illu">
            <div className="illu-row">
              <div className="illu-bar" />
              <div className="illu-dot" />
            </div>
            <div className="illu-row">
              <div className="illu-bar wide" />
            </div>
            <div className="illu-row">
              <div className="illu-bar" />
              <div className="illu-bar" />
            </div>
            <div className="illu-foot">Simulación de datos</div>
          </div>
        </aside>
      </section>
    </div>
  );
}
