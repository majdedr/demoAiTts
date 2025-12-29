from fastapi import APIRouter, BackgroundTasks
from app.services.ai_service import get_ai_response
from app.services.tts_service import speak
from app.services.stt_service import listen_from_mic
from app.models.schemas import ChatRequest
from app.core.config import IS_LOCAL

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest, background_tasks: BackgroundTasks):
    reply = get_ai_response(request.message)
    background_tasks.add_task(speak, reply)
    return {"response": reply}

@router.post("/voice_chat")
def voice_chat(background_tasks: BackgroundTasks):
    if not IS_LOCAL:
        return {"error": "Voice input available only in local mode"}

    user_text = listen_from_mic()
    reply = get_ai_response(user_text)
    background_tasks.add_task(speak, reply)

    return {"user_text": user_text, "response": reply}
