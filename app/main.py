# app/main.py

from builtins import Exception
import traceback
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from app.database import Database
from app.dependencies import get_settings
from app.routers import user_routes
from app.utils.api_description import getDescription

# Initialize FastAPI app
app = FastAPI(
    title="User Management",
    description=getDescription(),
    version="0.0.1",
    contact={
        "name": "API Support",
        "url": "http://www.example.com/support",
        "email": "support@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
        {"name": "Login and Registration", "description": "Endpoints related to user login and registration"},
        {"name": "User Management Requires (Admin or Manager Roles)", "description": "Endpoints for user management"},
    ],
)

# Database initialization on startup
@app.on_event("startup")
async def startup_event():
    settings = get_settings()
    Database.initialize(settings.database_url, settings.debug)

# Global exception handler
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred", "detail": str(traceback.format_exc())}
    )

# Include user routes
app.include_router(user_routes.router)

# Custom OpenAPI schema for Swagger token support (HTTPBearer)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "HTTPBearer": {
            "type": "http",
            "scheme": "bearer"
        }
    }
    openapi_schema["security"] = [{"HTTPBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Apply the custom OpenAPI schema
app.openapi = custom_openapi
