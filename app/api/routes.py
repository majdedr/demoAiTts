import logging
from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.services.ai_service import get_ai_response
from app.services.tts_service import speak
from app.services.stt_service import listen_from_mic
from app.models.schemas import ChatRequest
from app.core.config import IS_LOCAL
from app.core.error_handling import ServiceError

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest, background_tasks: BackgroundTasks):
    try:
        # Pydantic will validate request automatically
        reply = get_ai_response(request)
        background_tasks.add_task(speak, reply)
        return {"response": reply}
    except ServiceError as se:
        raise se
    except Exception as e:
        logging.exception("Unexpected error in /chat endpoint")
        raise ServiceError("Failed to process chat request.")


@router.post("/voice_chat")
def voice_chat(background_tasks: BackgroundTasks):
    if not IS_LOCAL:
        raise HTTPException(status_code=403, detail="Voice input available only in local mode")
    try:
        user_text = listen_from_mic()
        # Use default max_tokens for voice input
        request = ChatRequest(text=user_text, max_tokens=256)
        reply = get_ai_response(request)
        background_tasks.add_task(speak, reply)
        return {"user_text": user_text, "response": reply}
    except ServiceError as se:
        raise se
    except Exception as e:
        logging.exception("Unexpected error in /voice_chat endpoint")
        raise ServiceError("Failed to process voice chat request.")
