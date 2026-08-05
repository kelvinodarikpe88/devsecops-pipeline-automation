"""Minimal FastAPI app — the target for SAST and DAST scanning."""
from fastapi import FastAPI

app = FastAPI(title="Demo App")


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/health")
def health():
    return {"status": "healthy"}

