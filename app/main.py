from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from app.api.routes import keys, random,hashing,ecdsa,ecdh
app = FastAPI(
    title="ATECC608 Security API",
    description="Secure cryptographic API for IoT and blockchain applications",
    version="1.0.0"
)
app.include_router(keys.router)
app.include_router(random.router)
app.include_router(hashing.router)
app.include_router(ecdsa.router)
app.include_router(ecdh.router)

@app.get("/", response_class=HTMLResponse)
def root():

    dashboard_path = (
        Path(__file__).parent
        / "templates"
        / "dashboard.html"
    )
    return dashboard_path.read_text(
        encoding="utf-8"
    )
