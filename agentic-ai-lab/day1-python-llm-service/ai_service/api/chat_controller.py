from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ai_service.services.llm_service import LLMService, ask

router = APIRouter()

llm_service = LLMService()

class AskRequest(BaseModel):
    prompt: str


@router.post("/ask")
def ask_ai(req: AskRequest):

    try:
        answer = ask(req.prompt)
        return {"answer": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))