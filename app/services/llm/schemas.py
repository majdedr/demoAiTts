from pydantic import BaseModel
from typing import Optional


class LLMRequest(BaseModel):
    user_text: str
    context: Optional[str] = None
    temperature: float = 0.2


class LLMResponse(BaseModel):
    text: str
    model: str
    tokens_used: Optional[int] = None
