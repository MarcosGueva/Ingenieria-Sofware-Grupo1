import { useState } from "react";
import { registerUser } from "../api/auth";
import { useNavigate, Link } from "react-router-dom";

export default function Register() {
  const nav = useNavigate();
  const [form, setForm] = useState({ name:"", email:"", password:"" });
  const [msg, setMsg] = useState(""); const [err, setErr] = useState("");

  const onChange = e => setForm(f => ({...f, [e.target.name]: e.target.value}));

  async function onSubmit(e) {
    e.preventDefault(); setErr(""); setMsg("");
    try { await registerUser(form); setMsg("¡Cuenta creada!"); setTimeout(()=>nav("/login"), 800); }
    catch (e) { setErr(e.message); }
  }

  return (
    <div style={{maxWidth:420, margin:"4rem auto"}}>
      <h1>Registro</h1>
      <form onSubmit={onSubmit}>
        <label>Nombre</label>
        <input name="name" value={form.name} onChange={onChange} required/>
        <label>Email</label>
        <input name="email" type="email" value={form.email} onChange={onChange} required/>
        <label>Contraseña</label>
        <input name="password" type="password" value={form.password} onChange={onChange} required/>
        {err && <p style={{color:"crimson"}}>{err}</p>}
        {msg && <p style={{color:"green"}}>{msg}</p>}
        <button type="submit">Crear cuenta</button>
      </form>
      <p style={{marginTop:12}}>¿Ya tienes cuenta? <Link to="/login">Inicia sesión</Link></p>
    </div>
  );
}
