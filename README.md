# 🧠 Voice AI Demo – Local & Production Architecture

## Overview

This project is a **Voice AI demo application** designed to showcase how modern AI systems are structured for **local development** versus **production environments**.  

It demonstrates:

- AI orchestration logic  
- Voice pipelines (**STT → AI → TTS**)  
- Clean, modular backend architecture  
- Environment-aware design  
- Docker-ready production setup  

---

## Architecture Philosophy

In real-world systems:

- **Microphone access** belongs on the **client side**  
- **Backend services** must remain hardware-agnostic  
- **Containers** should be stateless and scalable  

This project reflects that philosophy by supporting **two modes**:

| Mode            | Purpose               | Features                     |
|-----------------|---------------------|-------------------------------|
| Local Dev Mode  | Demo & experimentation | 🎤 STT + 🧠 AI + 🔊 TTS        |
| Production Mode | Scalable backend      | 🧠 AI + API only               |

---

## Project Structure

demoAI/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── api/ # API routes (/chat, /voice_chat)
│ ├── services/ # AI, STT, TTS, VectorStore services
│ ├── models/ # Pydantic schemas (ChatRequest, LLMRequest, etc.)
│ ├── core/ # Environment configuration, error handling
│ └── init.py
│
├── requirements.txt # Production dependencies (AI backend only)
├── requirements.local.txt # Local dev dependencies (voice-enabled)
├── Dockerfile # Production-ready container
└── README.md


---

## Local Development (Voice Enabled)

Install dependencies

```bash
pip install -r requirements.local.txt


Set environment

$Env:ENV="local"


Run server

uvicorn app.main:app --reload


Test API

Open in browser:

http://127.0.0.1:8000/docs


Use:

POST /chat → Text interaction

POST /voice_chat → Voice interaction (microphone required)

Note: /voice_chat will record audio from your mic, convert it to text via STT, send it to the AI backend, then play TTS in the background.

Production Mode (Docker / Backend Only)

Audio hardware is excluded

API remains stateless and scalable

Suitable for cloud & GPU workloads

docker build -t voice-ai-backend .
docker run -p 8000:8000 voice-ai-backend


In production mode, /voice_chat is disabled. Only /chat (text) is available.

Key Engineering Concepts Demonstrated

Separation of concerns

Environment-based feature toggling (ENV=local vs production)

Background task processing (fastapi.BackgroundTasks)

Voice AI pipelines (STT → LLM → TTS)

Production-safe containerization

Clean Python project structure