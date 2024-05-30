import sqlite3
import os
import json
from core.config import settings

def update_json_file_in_static(json_path, json_data):
    with open(json_path, 'w') as fp:
        json.dump(json_data, fp)

def check_json_structure(json_str_data):
    print(json_str_data)
    try:
        parsed_json = eval(json_str_data)
        
        print("parsed_json::: ", parsed_json)
        print(type(parsed_json))
        if isinstance(parsed_json, dict):
            return parsed_json
        else:
            return False
    except json.JSONDecodeError:
        return False


def check_distributor_json_structure(json_str_data):
    distributor_original_key_list = sorted(["Id", "Label", "Title", "Description", "Main target", "Seo keywords", "Tone"])
    
    try:
        parsed_json = eval(json_str_data)
        print("~~ ~~ " * 20)
        for key in parsed_json.keys():
            print(parsed_json[key].keys())
            if sorted(parsed_json[key].keys()) == distributor_original_key_list:
                return True
            else:
                return False
    except json.JSONDecodeError:
        return False
    
    
def check_market_json_structure(json_str_data):
    market_original_key_list = sorted(["Id", "Title","Marketing_axis","Cultural_recommendations","Languages","SEO_keywords","Market_features"])
    
    try:
        parsed_json = eval(json_str_data)
        print("~~ ~~ " * 20)
        for key in parsed_json.keys():
            print(parsed_json[key].keys())
            if sorted(parsed_json[key].keys()) == market_original_key_list:
                return True
            else:
                return False
    except json.JSONDecodeError:
        return False
    
def check_product_json_structure(json_str_data):
    product_original_key_list = sorted(["Title", "Description", "Features_1", "features_2", "features_3", "Url"])
    
    try:
        parsed_json = eval(json_str_data)
        print("~~ ~~ " * 20)
        for key in parsed_json.keys():
            print(parsed_json[key].keys())
            if sorted(parsed_json[key].keys()) == product_original_key_list:
                return True
            else:
                return False
    except json.JSONDecodeError:
        return False

def get_features_json():
    with open(settings.FEATURES_JSON_PATH, 'r') as fp:
        return json.load(fp)
    
def get_distributors_json():
    with open(settings.DISTRIBUTORS_JSON_PATH, 'r') as fp:
        return json.load(fp)

def get_market_json():
    with open(settings.MARKET_JSON_PATH, 'r') as fp:
        return json.load(fp)
    
def get_marketing_axis_json():
    with open(settings.MARKET_AXIS_JSON_PATH, 'r') as fp:
        return json.load(fp)

def get_product_json():
    with open(settings.PRODUCTS_JSON_PATH, 'r') as fp:
        return json.load(fp)


def get_all_json_data():
    final_dict = {
        "product": get_product_json(),
        "marketAxis": get_marketing_axis_json(),
        "market": get_market_json(),
        "distribution": get_distributors_json(),
        "features": get_features_json()
    }
    return final_dict