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


@dis_mar_router.get('/get_one_distributor_version')
def get_one_distributor_version(distributor_version_id):
    return services.get_one_distributor_version(distributor_version_id)


@dis_mar_router.post('/distributor_prompt_generator')
def distributor_prompt_generator(distributor_id: int, local_master_id: int, distributor_settings: str):
    return services.distributor_prompt_generator(distributor_id, local_master_id, distributor_settings)


@dis_mar_router.post('/distributor_version_content_generator')
def distributor_version_content_generator(distributor_id: int, local_master_id: int, distributor_settings: str,
                                          prompt: str):
    return services.distributor_version_content_generator(distributor_id, local_master_id, distributor_settings, prompt)


@dis_mar_router.get('/list_distributor_versions')
def get_list_of_distributor_versions(local_master_id: int):
    return services.get_list_of_distributer_versions(local_master_id)
