import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI(title="PulseBoard API")

DATABASE_URL = os.getenv("DATABASE_URL", "not-set")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "pulseboard-api"}

@app.get("/")
def root():
    return {"message": "Welcome to PulseBoard"}

@app.get("/db-check")
def db_check():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"database": "connected", "url_host": DATABASE_URL.split("@")[-1]}
    except Exception as e:
        return {"database": "connection failed", "error": str(e)}
