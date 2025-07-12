# caja_ahorros_api/main.py

from fastapi import FastAPI
from caja_ahorros_api.controllers.auth_controller import router as auth_router
from caja_ahorros_api.controllers.ahorro_controller import router as ahorro_router
from caja_ahorros_api.controllers.credito_controller import router as credito_router
from caja_ahorros_api.controllers.reporte_controller import router as reporte_router
from caja_ahorros_api.controllers.auditoria_controller import router as auditoria_router
from caja_ahorros_api.controllers.socio_controller import router as socio_router
from caja_ahorros_api.controllers.ingreso_egreso_controller import router as ingreso_egreso_router
from caja_ahorros_api.controllers.reporte_ingreso_egreso_controller import router as reporte_ingreso_egreso_router

app = FastAPI(title="API Caja de Ahorros")

app.include_router(auth_router,      prefix="/auth",                         tags=["Autenticación"])
app.include_router(ahorro_router,    prefix="/ahorros",                      tags=["Ahorros"])
app.include_router(credito_router,   prefix="/creditos",                     tags=["Créditos"])
app.include_router(reporte_router,   prefix="/reportes",                     tags=["Reportes"])
app.include_router(auditoria_router, prefix="/auditoria",                    tags=["Auditoría"])
app.include_router(socio_router,     prefix="/socios",                       tags=["Socios"])
app.include_router(ingreso_egreso_router,
                   prefix="/ingresos-egresos",              tags=["Ingresos y Egresos"])
app.include_router(reporte_ingreso_egreso_router,
                   prefix="/reportes-ingresos-egresos",     tags=["Reportes Ingresos y Egresos"])

