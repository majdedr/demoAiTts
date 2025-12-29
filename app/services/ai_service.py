conversation_history = []

def get_ai_response(user_text: str) -> str:
    conversation_history.append({"role": "user", "content": user_text})

    # Mock AI (safe for demo)
    ai_reply = f"AI response to: {user_text}"

    conversation_history.append({"role": "assistant", "content": ai_reply})
    return ai_reply
