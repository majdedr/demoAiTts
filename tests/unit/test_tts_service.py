import pytest
from unittest.mock import patch
from app.services import tts_service
from app.core.error_handling import ServiceError


def test_tts_speak_success():
    with patch("app.services.tts_service.pyttsx3.init") as mock_engine:
        mock_engine.return_value.say.return_value = None
        mock_engine.return_value.runAndWait.return_value = None
        tts_service.speak("Hello world")
        mock_engine.return_value.say.assert_called_with("Hello world")


def test_tts_speak_empty_text_raises_error():
    from app.core.error_handling import ServiceError
    from unittest.mock import patch
    from app.services import tts_service

    # Patch pyttsx3 to raise ServiceError on empty text
    with patch("app.services.tts_service.pyttsx3.init") as mock_engine:
        mock_engine.return_value.say.side_effect = ServiceError(
            "Text-to-speech text is empty")
        with pytest.raises(ServiceError):
            tts_service.speak("")
