🧠 Voice AI Demo – Local & Production Architecture

Overview

This project is a Voice AI demo application built to demonstrate how modern AI systems are structured in local development versus production environments.

It showcases:

AI orchestration logic

Voice pipelines (STT → AI → TTS)

Clean backend architecture

Environment-aware design

Docker-ready production setup

Architecture Philosophy

In real-world systems:

Microphone access belongs on the client side

Backend services must remain hardware-agnostic

Containers should be stateless and scalable

This project reflects that philosophy by supporting two modes:

Mode	Purpose	Features
Local Dev Mode	Demo & experimentation	🎤 STT + 🧠 AI + 🔊 TTS
Production Mode	Scalable backend	🧠 AI + API only
Project Structure
demoAI/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── api/                 # API routes
│   ├── services/            # AI, STT, TTS services
│   ├── models/              # Pydantic schemas
│   ├── core/                # Environment config
│   └── __init__.py
│
├── requirements.txt         # Production dependencies
├── requirements.local.txt   # Local (voice-enabled) dependencies
├── Dockerfile
└── README.md

Local Development (Voice Enabled)
Install dependencies
pip install -r requirements.local.txt

Set environment
$Env:ENV="local"

Run server
uvicorn app.main:app --reload

Test

Open:

http://127.0.0.1:8000/docs


Use:

POST /chat → text interaction

POST /voice_chat → voice interaction (microphone required)

Production Mode (Docker / Backend Only)

Microphone and audio hardware are excluded

API remains stateless and scalable

Suitable for cloud & GPU workloads

docker build -t voice-ai-backend .
docker run -p 8000:8000 voice-ai-backend

Key Engineering Concepts Demonstrated

Separation of concerns

Environment-based feature toggling

Background task processing

Voice AI pipelines

Production-safe containerization

Clean Python project structure

Why This Matters

This project mirrors how real AI systems are built:

Client handles audio capture

Backend focuses on orchestration and intelligence

Docker images remain portable and scalable
