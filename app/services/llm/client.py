from ctransformers import AutoModelForCausalLM
from app.services.llm.schemas import LLMRequest


class LLMClient:
    def __init__(self, model_path: str):
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            model_type="llama",
            gpu_layers=0,        # CPU safe
            context_length=2048
        )

    async def generate(self, request: LLMRequest):
        # Extract just the text (and optionally append context)
        prompt = request.user_text
        if request.context:
            prompt = f"{request.context}\n\n{prompt}"

        # Pass the string to the model, not the LLMRequest object
        result = self.model(
            prompt,
            temperature=request.temperature
        )

        return result
