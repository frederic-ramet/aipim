from fastapi import APIRouter
from core.apps.content_creation import services
from core.config import settings


cc_router = APIRouter(
    prefix=str(settings.API_VERSION_STR),
    tags=["User Management API"]
)

@cc_router.get('/scrap_data')
def scrap_content(product_url: str):
    return services.scrap_content_form_url(product_url)


@cc_router.post('/generate_prompt')
def generate_prompt_local(scraped_data: str, selected_market:str):
    return services.generate_prompt_local(scraped_data, selected_market)


@cc_router.post('/generate_content')
def generate_content_local(prompt:str):
    return services.generate_content_local(prompt)