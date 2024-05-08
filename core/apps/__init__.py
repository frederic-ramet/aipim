from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.apps.users_management import routes as users_management_router
from core.apps.clients_management import routes as clients_management_router
from core.apps.app_management import routes as app_management_router
from core.apps.llm_services import routes as llm_services_router
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
    app.include_router(users_management_router.auth_router)
    app.include_router(users_management_router.um_router)
    app.include_router(clients_management_router.client_router)
    app.include_router(app_management_router.app_router)
    app.include_router(app_management_router.logs_router)
    app.include_router(llm_services_router.llm_router)

    return app
