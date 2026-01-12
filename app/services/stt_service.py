import logging
import speech_recognition as sr
from app.core.error_handling import ServiceError


def transcribe_audio(recognizer: sr.Recognizer, audio: sr.AudioData) -> str:
    """
    Pure STT logic:
    - No microphone access
    - Fully testable
    """

    try:
        return recognizer.recognize_google(audio)
    except Exception as e:
        logging.exception("STT transcription failed")
        raise ServiceError("Speech-to-text transcription failed.") from e


def listen_from_mic(timeout: int = 5) -> str:
    """
    I/O layer:
    - Talks to microphone
    - NOT unit tested
    """

    try:
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=timeout)

        # Delegate transcription to pure function
        return transcribe_audio(recognizer, audio)

    except Exception as e:
        logging.exception("STT service failed")
        raise ServiceError("Speech-to-text service failed.") from e
