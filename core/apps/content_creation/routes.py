from fastapi import APIRouter
from core.apps.content_creation import services
from core.config import settings



lm_router = APIRouter(
    prefix=str(settings.API_VERSION_STR),
    tags=["Local Master Managment"]
)

@lm_router.post('/generate_prompt')
def generate_prompt_local(scraped_data: str, selected_market:str):
    return services.generate_prompt_local(scraped_data, selected_market)


@lm_router.post('/generate_content')
def generate_content_local(prompt:str):
    return services.generate_content_local(prompt)