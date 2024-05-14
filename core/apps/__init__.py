from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.apps.content_creation import routes as content_creation_router
from core.config import settings


def create_app() -> FastAPI:
    """
    Creating a FastAPI instance and registering routes.
    """

    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )

    # CORS Configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Registering routes
    app.include_router(content_creation_router.cc_router)
    

    return app
