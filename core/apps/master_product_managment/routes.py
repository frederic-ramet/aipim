from fastapi import APIRouter
from core.apps.master_product_managment import services
from core.config import settings


mp_router = APIRouter(
    prefix=str(settings.API_VERSION_STR),
    tags=["Master Product Managment"]
)

@mp_router.get('/list_master_products')
def list_master_products():
    return services.list_master_products()

@mp_router.get('/scrap_data')
def scrap_content(product_url: str):
    return services.scrap_content_form_url(product_url)
