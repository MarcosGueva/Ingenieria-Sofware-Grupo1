import { createContext, useContext, useState } from "react";
import { isAuthenticated, logout as doLogout } from "../api/auth";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [authed, setAuthed] = useState(isAuthenticated());

  const login = () => setAuthed(true);
  const logout = () => { doLogout(); setAuthed(false); };

  return (
    <AuthContext.Provider value={{ authed, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
export function useAuth() { return useContext(AuthContext); }
