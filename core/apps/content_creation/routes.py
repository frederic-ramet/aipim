from fastapi import APIRouter
from core.apps.content_creation import services
from core.config import settings

lm_router = APIRouter(
    prefix=str(settings.API_VERSION_STR),
    tags=["Local Master Managment"]
)

@lm_router.post('/generate_prompt')
def generate_prompt_local(master_product_id:int, selected_market:str):
    return services.generate_prompt_local(master_product_id, selected_market)

@lm_router.post('/generate_content')
def generate_content_local(local_master_id:int):
    return services.generate_content_local(local_master_id)

@lm_router.get('/list_local_products')
def get_list_of_local_products(master_product_id:str):
    return services.get_list_of_local_products(master_product_id)