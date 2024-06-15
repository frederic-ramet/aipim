from core.apps.database_creation_changes import utils
from core.config import settings

from create_database import update_configuration_database

import sqlite3
import json
import os


def update_features_json_file(json_str_data):
    if utils.check_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.FEATURES_JSON_PATH
        return utils.update_json_file_in_static(json_path, json_data, "")
    else:
        return {"status": 500, "message": "json structure is not correct"}


def update_marketing_axis_json_file(json_str_data):
    if utils.check_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.MARKET_AXIS_JSON_PATH
        return utils.update_json_file_in_static(json_path, json_data, "")
    else:
        return {"status": 500, "message": "json structure is not correct"}

def update_distributors_json_file(json_str_data):
    if utils.check_distributor_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.DISTRIBUTORS_JSON_PATH
        return utils.update_json_file_in_static(json_path, json_data, "distributor")
    else:
        return {"status": 500, "message": "json structure is not correct"}
    
def update_market_json_file(json_str_data):
    if utils.check_market_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.MARKET_JSON_PATH
        return utils.update_json_file_in_static(json_path, json_data, "market")
    else:
        return {"status": 500, "message": "json structure is not correct"}

def update_product_json_file(json_str_data):
    if utils.check_product_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.PRODUCTS_JSON_PATH
        return utils.update_json_file_in_static(json_path, json_data, "")
    else:
        return {"status": 500, "message": "json structure is not correct"}
    

def update_prompt_master_json_file(json_str_data):
    if utils.check_json_structure(json_str_data):
        json_data = eval(json_str_data)
        json_path = settings.PROMPT_MASTER_JSON_PATH 
        return utils.update_json_file_in_static(json_path, json_data, "")
    else:
        return {"status": 500, "message": "json structure is not correct"}

def store_configuration(config_name):
    update_configuration_database(config_name)
        

def get_configurations(config_id="all"):
    conn = sqlite3.connect(settings.DB_PATH)
    cursor = conn.cursor()

    if config_id != "all":
        # SQL command for retrieving a specific configuration by ID
        sql = '''
            SELECT * FROM configurations WHERE id = ?
        '''
        cursor.execute(sql, (config_id,))
    else:
        # SQL command for retrieving all configurations
        sql = '''
            SELECT * FROM configurations
        '''
        cursor.execute(sql)

    configurations = cursor.fetchall()
    conn.close()
    print('configurations')    
    return configurations


# def update_database_data():
#     return utils.update_database_data()