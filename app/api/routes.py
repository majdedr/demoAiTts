import logging
from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.services.ai_service import get_ai_response
from app.services.tts_service import speak
from app.services.stt_service import listen_from_mic
from app.models.schemas import ChatRequest
from app.core.config import IS_LOCAL
from app.core.error_handling import ServiceError
from app.services.llm.schemas import LLMRequest

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest, background_tasks: BackgroundTasks):
    try:
        # Convert ChatRequest -> LLMRequest
        llm_request = LLMRequest(
            user_text=request.text,        # map .text → .user_text
            context=getattr(request, "context", None),  # optional
            temperature=getattr(request, "temperature", 0.2)
        )

        # Await async AI service
        reply = await get_ai_response(llm_request)

        # Run TTS in background (non-blocking)
        background_tasks.add_task(speak, reply)

        return {"response": reply}

    except ServiceError as se:
        raise se
    except Exception:
        logging.exception("Unexpected error in /chat endpoint")
        raise ServiceError("Failed to process chat request.")


@router.post("/voice_chat")
async def voice_chat(background_tasks: BackgroundTasks):
    if not IS_LOCAL:
        raise HTTPException(
            status_code=403,
            detail="Voice input available only in local mode",
        )

    try:
        # STT is blocking → OK for local demo
        user_text = listen_from_mic()

        # Convert to LLMRequest
        llm_request = LLMRequest(
            user_text=user_text,
            temperature=0.2  # or any value you want
        )

        # Await async AI service
        reply = await get_ai_response(llm_request)

        # Run TTS in background
        background_tasks.add_task(speak, reply)

        return {
            "user_text": user_text,
            "response": reply,
        }

    except ServiceError as se:
        raise se
    except Exception:
        logging.exception("Unexpected error in /voice_chat endpoint")
        raise ServiceError("Failed to process voice chat request.")
