from fastapi import FastAPI
from ai_service.api.chat_controller import router

app = FastAPI(title="AI Service")

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}