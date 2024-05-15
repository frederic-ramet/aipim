from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.apps.content_creation import routes as content_creation_router
from core.apps.master_product_managment import routes as master_product_router 
from core.apps.distributor_market_managment import routes as distributor_market_router 
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
    app.include_router(master_product_router.mp_router)
    app.include_router(content_creation_router.lm_router)
    app.include_router(distributor_market_router.dis_mar_router)
    

    return app
