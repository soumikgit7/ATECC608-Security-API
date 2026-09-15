from fastapi import FastAPI

from app.api.routes import keys, random,hashing


app = FastAPI(
    title="ATECC608 Security API",
    description="Secure cryptographic API for IoT and blockchain applications",
    version="1.0.0"
)


app.include_router(keys.router)
app.include_router(random.router)
app.include_router(hashing.router)


@app.get("/")
def root():
    return {
        "message": "ATECC608 Security API is running"
    }