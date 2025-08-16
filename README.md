Caja de Ahorros 💳

Sistema web para gestionar socios, ahorros, créditos y control de roles.
Frontend en React (Vite) y Backend en FastAPI con MongoDB.

👥 Integrantes del Grupo

Marcos Guevara

Kenneth Vera

Ricardo Peña

Génesis Gusñay

🧩 Tareas asignadas
Backend

Ricardo Peña → refactor y ajustes en controllers/ y services/.

Kenneth Vera → actualización de repositories/, schemas/ y del archivo de entrada main.

Génesis Gusñay → actualización de models/ y configuración en config/.

🧩 Frontend (creación y configuración)

Génesis Gusñay → creación de App.jsx y App.css.

Ricardo Peña → creación de la carpeta context/ y el archivo index.css.

Kenneth Vera → creación de main.jsx y estructura de components/.

Marcos Guevara → creación de pages/ y configuración de la conexión backend ⇄ frontend (consumo de API).

Nota: Los nombres de carpetas/archivos se listan tal como existen en el proyecto para facilitar su verificación.

🚀 Características

Autenticación (registro/login) con JWT

Gestión de socios (CRUD)

Ahorros: depósitos / retiros con control de saldo

Créditos: solicitud, aprobación y tabla de amortización

Ingresos/Egresos (contabilidad simple)

Roles: Admin y Empleado (control de acceso por rol)

Validación con Pydantic

📦 Tecnologías

Frontend

React + Vite, React Router, React Bootstrap

Axios, localStorage

Backend

FastAPI, Uvicorn

MongoDB (motor async)

Pydantic, passlib (hash), python-jose (JWT)

reportlab (PDF), openpyxl (Excel)

Pytest (tests)

✅ Requisitos

Node.js 18+

Python 3.10+

MongoDB (local o Atlas)