
from pydantic import BaseModel, model_validator

class ChatRequest(BaseModel):
    text: str
    max_tokens: int

    @model_validator(mode="after")
    def validate_limits(self):
        if len(self.text) > 4000 and self.max_tokens > 1024:
            raise ValueError("Input too long for requested token count")
        return self
