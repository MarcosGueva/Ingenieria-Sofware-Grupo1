import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, useLocation } from "react-router-dom";
import App from "./App.jsx";
import "./index.css";
import { AuthProvider } from "./context/AuthContext.jsx";

/* --- 1) Basename configurable ---
   Si despliegas bajo /app o GitHub Pages, define VITE_BASE_PATH="/app"
   y el router ajusta todas las rutas. En local no afecta. */
const BASENAME = import.meta.env.VITE_BASE_PATH || "/";

/* --- 2) ScrollToTop: sube al top en cada navegación --- */
function ScrollToTop() {
  const { pathname } = useLocation();
  React.useEffect(() => {
    window.scrollTo({ top: 0, left: 0, behavior: "instant" });
  }, [pathname]);
  return null;
}

/* --- 3) ErrorBoundary muy simple --- */
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, err: null };
  }
  static getDerivedStateFromError(err) {
    return { hasError: true, err };
  }
  componentDidCatch(err, info) {
    // Aquí podrías enviar el error a un servicio (Sentry, etc.)
    console.error("ErrorBoundary:", err, info);
  }
  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: 24, color: "#e7e9ee" }}>
          <h2>Algo salió mal 😵</h2>
          <p>Intenta recargar la página o volver al inicio.</p>
          <button className="auth-btn" onClick={() => location.reload()}>
            Recargar
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter basename={BASENAME}>
      <AuthProvider>
        <ScrollToTop />
        <ErrorBoundary>
          <App />
        </ErrorBoundary>
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
