from fastapi import APIRouter
from core.apps.content_creation import services
from core.config import settings


cc_router = APIRouter(
    prefix=str(settings.API_VERSION_STR),
    tags=["User Management API"]
)

@cc_router.post('/scrap_data')
def scrap_content(product_url: str):
    return services.scrap_content_form_url(product_url)

