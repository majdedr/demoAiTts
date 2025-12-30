
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.core.error_handling import (
	setup_logging, service_error_handler, ServiceError, http_exception_handler
)

app = FastAPI(title="Voice AI Demo")

# Setup logging
setup_logging()

# Add CORS middleware (allow all for demo, restrict in prod)
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Register error handlers
app.add_exception_handler(ServiceError, service_error_handler)
app.add_exception_handler(RequestValidationError, lambda req, exc: JSONResponse(status_code=422, content={"error": str(exc)}))
app.add_exception_handler(Exception, lambda req, exc: JSONResponse(status_code=500, content={"error": "Internal server error"}))
app.add_exception_handler(HTTPException, http_exception_handler)

app.include_router(router)
