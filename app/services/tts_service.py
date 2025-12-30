import logging
import pyttsx3
from app.core.error_handling import ServiceError

def speak(text: str):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        logging.exception("TTS service failed")
        raise ServiceError("Text-to-speech service failed.")
