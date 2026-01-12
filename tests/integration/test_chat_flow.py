import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)


def test_voice_chat_local_mode(monkeypatch):
    # Force local mode so voice_chat works
    monkeypatch.setattr("app.core.config.IS_LOCAL", True)

    # Mock listen_from_mic to return fixed text
    with patch("app.api.routes.listen_from_mic", return_value="Hi there"):

        # Mock TTS so it does nothing
        with patch("app.services.tts_service.speak"):
            response = client.post("/voice_chat")

    assert response.status_code == 200
    json_data = response.json()
    assert json_data["user_text"] == "Hi there"
    assert "AI response" in json_data["response"]
