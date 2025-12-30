import logging
import speech_recognition as sr
from app.core.error_handling import ServiceError

def listen_from_mic(timeout=5) -> str:
    try:
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=timeout)
        return recognizer.recognize_google(audio)
    except Exception as e:
        logging.exception("STT service failed")
        raise ServiceError("Speech-to-text service failed.")
