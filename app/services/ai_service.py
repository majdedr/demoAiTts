import logging
from typing import List, Dict

from app.core.error_handling import ServiceError
from app.models.schemas import ChatRequest

from app.services.llm import LLMClient, LLMRequest
from app.services.vector_store import vector_store
from app.services.llm.schemas import LLMResponse


logger = logging.getLogger(__name__)

# Simple in-memory conversation history (per process)
conversation_history: List[Dict[str, str]] = []

# Initialize LLM once (important for performance)
llm = LLMClient(
    r"C:\Users\user1\Desktop\demoAiGetRepo\demoAiTts\app\models\tinyllama-1.1b-chat-v1.0.Q4_K_S.gguf"
)


async def get_ai_response(request: LLMRequest) -> LLMResponse:
    try:
        # Call your LLM client
        llm_response = await llm.generate(request)  # returns a string

        # Wrap it in the response model
        response = LLMResponse(
            text=llm_response,  # the string
            model="TinyLlama-1.1B",  # or whatever model you are using
            tokens_used=None  # optional, if you track tokens
        )

        return response

    except Exception as e:
        logger.error("AI service failed", exc_info=True)
        raise ServiceError("AI service failed to generate a response.") from e
