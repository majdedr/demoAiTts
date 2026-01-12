import pytest
from app.services.ai_service import get_ai_response
from app.models.schemas import ChatRequest
from app.core.error_handling import ServiceError


def test_ai_service_returns_response():
    """
    Happy path test:
    - Valid input
    - AI service returns a response
    """
    request = ChatRequest(text="Hello AI", max_tokens=100)

    response = get_ai_response(request)

    assert isinstance(response, str)
    assert "Hello AI" in response


def test_ai_service_invalid_input_raises_error():
    """
    Error path test:
    - Invalid input
    - ServiceError is raised
    """
    bad_request = {
        "text": "",
        "max_tokens": -10
    }

    with pytest.raises(ServiceError):
        get_ai_response(bad_request)
