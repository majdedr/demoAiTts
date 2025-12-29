import speech_recognition as sr

def listen_from_mic(timeout=5) -> str:
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=timeout)

    try:
        return recognizer.recognize_google(audio)
    except Exception:
        return "Sorry, I could not understand."
