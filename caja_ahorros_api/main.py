from fastapi import FastAPI
from controllers.auth_controller import router as auth_router

app = FastAPI(title="API Caja de Ahorros")

app.include_router(auth_router, prefix="/auth", tags=["Autenticación"])