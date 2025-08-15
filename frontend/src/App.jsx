import { Routes, Route, Link } from "react-router-dom";
import ProtectedRoute from "./components/ProtectedRoute";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";

export default function App() {
  return (
    <>
      <nav style={{padding:"10px", borderBottom:"1px solid #eee"}}>
        <Link to="/">Inicio</Link>{" | "}
        <Link to="/login">Login</Link>{" | "}
        <Link to="/register">Registro</Link>
      </nav>

      <Routes>
        <Route path="/login" element={<Login/>} />
        <Route path="/register" element={<Register/>} />
        <Route path="/" element={
          <ProtectedRoute>
            <Dashboard/>
          </ProtectedRoute>
        } />
      </Routes>
    </>
  );
}
