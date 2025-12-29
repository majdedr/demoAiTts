from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Voice AI Demo")

app.include_router(router)
