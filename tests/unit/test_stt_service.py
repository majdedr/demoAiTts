import pytest
from unittest.mock import Mock, patch
from app.services import stt_service
from app.core.error_handling import ServiceError


def test_listen_from_mic_success():
    with patch("app.services.stt_service.sr.Recognizer") as mock_recognizer:
        mock_instance = mock_recognizer.return_value
        mock_instance.listen.return_value = "audio"
        mock_instance.recognize_google.return_value = "Hello mic"

        result = stt_service.listen_from_mic()
        assert result == "Hello mic"


def test_listen_from_mic_failure():
    with patch("app.services.stt_service.sr.Recognizer") as mock_recognizer:
        mock_instance = mock_recognizer.return_value
        mock_instance.listen.side_effect = Exception("Mic error")
        with pytest.raises(ServiceError):
            stt_service.listen_from_mic()
