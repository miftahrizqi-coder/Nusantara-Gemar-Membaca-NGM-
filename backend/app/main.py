from fastapi import FastAPI
from app.database import check_database_connection
from app.routes.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)

@app.get("/health")
def health_check():
    database_ok = check_database_connection()
    return {
        "status": "ok" if database_ok else "error",
        "database": "connected" if database_ok else "disconnected",
    }