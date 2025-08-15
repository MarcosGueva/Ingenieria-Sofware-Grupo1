# caja_ahorros_api/main.py


import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(filename=".env", usecwd=True), override=True)

from caja_ahorros_api.config.database import db
from caja_ahorros_api.services.auth_service import ensure_indexes

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from caja_ahorros_api.controllers.auth_controller import router as auth_router
from caja_ahorros_api.controllers.ahorro_controller import router as ahorro_router
from caja_ahorros_api.controllers.credito_controller import router as credito_router
from caja_ahorros_api.controllers.reporte_controller import router as reporte_router
from caja_ahorros_api.controllers.auditoria_controller import router as auditoria_router
from caja_ahorros_api.controllers.socio_controller import router as socio_router
from caja_ahorros_api.controllers.ingreso_egreso_controller import router as ingreso_egreso_router
from caja_ahorros_api.controllers.reporte_ingreso_egreso_controller import router as reporte_ingreso_egreso_router

from caja_ahorros_api.services.auth_service import ensure_indexes

app = FastAPI(title="API Caja de Ahorros")


ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
]
# --- CORS: permitir llamadas desde Vite (frontend) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # URL del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    print("[DB] MONGO_URI =", os.getenv("MONGO_URI"))
    # ping: si falla aquí, verás el error exacto de conexión
    await db.command("ping")
    await ensure_indexes()

# --- Routers ---
app.include_router(auth_router,      prefix="/auth",                         tags=["Autenticación"])
app.include_router(ahorro_router,    prefix="/ahorros",                      tags=["Ahorros"])
app.include_router(credito_router,   prefix="/creditos",                     tags=["Créditos"])
app.include_router(reporte_router,   prefix="/reportes",                     tags=["Reportes"])
app.include_router(auditoria_router, prefix="/auditoria",                    tags=["Auditoría"])
app.include_router(socio_router,     prefix="/socios",                       tags=["Socios"])
app.include_router(ingreso_egreso_router,         prefix="/ingresos-egresos",          tags=["Ingresos y Egresos"])
app.include_router(reporte_ingreso_egreso_router, prefix="/reportes-ingresos-egresos", tags=["Reportes Ingresos y Egresos"])

# --- Startup: índices y tareas iniciales ---
@app.on_event("startup")
async def on_startup():
    # Crea índice único en users.email (idempotente)
    await ensure_indexes()

# (Opcional) healthcheck rápido
@app.get("/")
def root():
    return {"message": "Backend activo"}