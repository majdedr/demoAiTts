
import logging
from app.core.error_handling import ServiceError
from app.models.schemas import ChatRequest

conversation_history = []

def get_ai_response(request: ChatRequest) -> str:
    try:
        # Validate request (pydantic will auto-validate, but explicit call for clarity)
        request = ChatRequest(**request.dict()) if not isinstance(request, ChatRequest) else request
        conversation_history.append({"role": "user", "content": request.text})
        # Mock AI
        ai_reply = f"AI response to: {request.text} (max_tokens={request.max_tokens})"
        conversation_history.append({"role": "assistant", "content": ai_reply})
        return ai_reply
    except Exception as e:
        logging.exception("AI service failed")
        raise ServiceError("AI service failed to generate a response.")
