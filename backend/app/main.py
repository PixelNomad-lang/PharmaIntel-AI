from fastapi import FastAPI

app = FastAPI(
    title="PharmaIntel AI",
    version="0.1.0",
    description="AI Powered Pharma Sales Intelligence Platform"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to PharmaIntel AI"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }