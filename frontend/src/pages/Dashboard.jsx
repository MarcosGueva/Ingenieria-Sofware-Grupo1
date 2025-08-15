import { useEffect, useState } from "react";
import { api } from "../api/client";
import { useAuth } from "../context/AuthContext";

export default function Dashboard() {
  const { logout } = useAuth();
  const [text, setText] = useState("Cargando…");
  const [err, setErr] = useState("");

  useEffect(() => {
    let live = true;
    api.get("/socios/listar")  // cambia por una ruta protegida que tengas
      .then(d => live && setText(`Socios: ${Array.isArray(d)? d.length : "-"}`))
      .catch(e => live && setErr(e.message));
    return () => { live = false; };
  }, []);

  return (
    <div style={{maxWidth:720, margin:"2rem auto"}}>
      <div style={{display:"flex", justifyContent:"space-between"}}>
        <h1>Panel</h1>
        <button onClick={logout}>Cerrar sesión</button>
      </div>
      {err ? <p style={{color:"crimson"}}>{err}</p> : <p>{text}</p>}
    </div>
  );
}
