import pytest


class MockAIService:
    """
    Fake AI service used in tests instead of real AI.
    """

    async def generate(self, text: str) -> str:
        return f"Mock AI response to {text}"


@pytest.fixture
def mock_ai_service():
    """
    Pytest fixture:
    - Provides MockAIService instance
    - Automatically injected into tests
    """
    return MockAIService()
