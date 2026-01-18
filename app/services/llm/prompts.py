from typing import Optional
BASE_SYSTEM_PROMPT = """
You are a helpful, concise voice assistant.
Answer clearly and briefly.
"""

USER_PROMPT_TEMPLATE = """
User said:
{user_text}
"""


def build_prompt(user_text: str, context: Optional[str] = None) -> str:
    prompt = BASE_SYSTEM_PROMPT.strip()

    if context:
        prompt += f"\n\nContext:\n{context.strip()}"

    prompt += USER_PROMPT_TEMPLATE.format(user_text=user_text)

    return prompt
