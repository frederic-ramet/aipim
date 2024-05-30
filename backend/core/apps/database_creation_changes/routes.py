from fastapi import APIRouter
from core.apps.database_creation_changes import services
from core.apps.database_creation_changes import utils
from core.config import settings

db_router = APIRouter(
    prefix=str(settings.API_VERSION_STR),
    tags=["create new database "]
)

@db_router.post('/update_features_json_file')
def update_features_json_file(json_data):
    return services.update_features_json_file(json_data)

@db_router.post('/update_distributors_json_file')
def update_distributors_json_file(json_data):
    return services.update_distributors_json_file(json_data)

@db_router.post('/update_market_json_file')
def update_market_json_file(json_data):
    return services.update_market_json_file(json_data)

@db_router.post('/update_marketing_axis_json_file')
def update_marketing_axis_json_file(json_data):
    return services.update_marketing_axis_json_file(json_data)

@db_router.post('/update_product_json_file')
def update_product_json_file(json_data):
    return services.update_product_json_file(json_data)

@db_router.get('/get_features')
def get_features_json():
    return utils.get_features_json()

@db_router.get('/get_distributors')
def get_distributors_json():
    return utils.get_distributors_json()

# @db_router.get('/get_market')
# def get_market_json():
#     return utils.get_market_json()

# @db_router.get('/get_marketing_axis')
# def get_marketing_axis_json():
#     return utils.get_marketing_axis_json()

# @db_router.get('/get_product')
# def get_product_json():
#     return utils.get_product_json()

@db_router.get('/get_all_data')
def get_all_json_data():
    return utils.get_all_json_data()
# @db_router.post('/update_database_data')
# def update_database_data():
#     return services.update_database_data()