from core.apps.database_creation_changes import utils
from core.config import settings


def update_features_json_file(json_str_data):
    if utils.check_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.FEATURES_JSON_PATH
        return utils.update_json_file_in_static(json_path, json_data)
    else:
        return {"error": "json structure is not correct"}


def update_marketing_axis_json_file(json_str_data):
    if utils.check_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.MARKET_AXIS_JSON_PATH
        return utils.update_json_file_in_static(json_path, json_data)
    else:
        return {"error": "json structure is not correct"}


def update_distributors_json_file(json_str_data):
    if utils.check_distributor_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.DISTRIBUTORS_JSON_PATH
        return utils.update_json_file_in_static(json_path, json_data)
    else:
        return {"error": "json structure is not correct"}


def update_market_json_file(json_str_data):
    if utils.check_market_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.MARKET_JSON_PATH
        return utils.update_json_file_in_static(json_path, json_data)
    else:
        return {"error": "json structure is not correct"}


def update_product_json_file(json_str_data):
    if utils.check_product_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.PRODUCTS_JSON_PATH
        return utils.update_json_file_in_static(json_path, json_data)
    else:
        return {"error": "json structure is not correct"}


def update_database_data():
    return utils.update_database_data()
