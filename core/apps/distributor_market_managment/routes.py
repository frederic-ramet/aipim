from fastapi import APIRouter
from core.apps.distributor_market_managment import services
from core.config import settings


dis_mar_router = APIRouter(
    prefix=str(settings.API_VERSION_STR),
    tags=["Distributor market management"]
)

@dis_mar_router.get('/list_markets')
def list_markets():
    return services.list_markets()

@dis_mar_router.get('/list_distributors')
def list_distributors():
    return services.list_distributors()


@dis_mar_router.get('/distributor_prompt_generator')
def distributor_prompt_generator(distributor_id:int, local_master_id:int):
    return services.distributor_prompt_generator(distributor_id, local_master_id)


@dis_mar_router.get('/distributor_version_content_generator')
def distributor_version_content_generator(distributor_id:int):
    return services.distributor_version_content_generator(distributor_id)
