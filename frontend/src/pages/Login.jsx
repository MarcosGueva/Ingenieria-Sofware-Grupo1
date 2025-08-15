import { useState } from "react";
import { login as doLogin } from "../api/auth";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Login() {
  const nav = useNavigate();
  const { login } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState("");

  async function onSubmit(e) {
    e.preventDefault();
    setErr("");
    try { await doLogin(email, password); login(); nav("/"); }
    catch (e) { setErr(e.message); }
  }

  return (
    <div style={{maxWidth:420, margin:"4rem auto"}}>
      <h1>Iniciar sesión</h1>
      <form onSubmit={onSubmit}>
        <label>Email</label>
        <input type="email" value={email} onChange={e=>setEmail(e.target.value)} required/>
        <label>Contraseña</label>
        <input type="password" value={password} onChange={e=>setPassword(e.target.value)} required/>
        {err && <p style={{color:"crimson"}}>{err}</p>}
        <button type="submit">Entrar</button>
      </form>
      <p style={{marginTop:12}}>¿No tienes cuenta? <Link to="/register">Regístrate</Link></p>
    </div>
  );
}
