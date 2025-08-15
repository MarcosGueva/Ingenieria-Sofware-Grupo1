// src/App.jsx
import { Fragment } from "react";
import { Routes, Route, NavLink } from "react-router-dom";

import ProtectedRoute from "./components/ProtectedRoute";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";

export default function App() {
  return (
    <Fragment>
      {/* Barra superior */}
      <header className="app-header">
        <nav className="app-nav">
          <NavLink to="/" end className="app-link">
            Inicio
          </NavLink>
          <NavLink to="/login" className="app-link">
            Login
          </NavLink>
          <NavLink to="/register" className="app-link">
            Registro
          </NavLink>
          {/* opcional: deja el enlace si quieres acceso directo al panel */}
          <NavLink to="/dashboard" className="app-link">
            Dashboard
          </NavLink>
        </nav>
      </header>

      {/* Contenido principal */}
      <main className="app-main">
        <Routes>
          {/* Portada pública */}
          <Route path="/" element={<Home />} />

          {/* Rutas públicas */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          {/* Ruta protegida */}
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />

          {/* Fallback: si no existe la ruta, te llevo a Home */}
          <Route path="*" element={<Home />} />
        </Routes>
      </main>
    </Fragment>
  );
}
