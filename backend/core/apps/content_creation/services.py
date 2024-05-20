from core.apps.content_creation import utils
from core import utils as core_utils
from core.config import settings

ai_service_obj = core_utils.aiService()

def generate_prompt_local(master_product_id:int, selected_market_id:int, market_settings:str):
    get_scrapped_data = utils.get_scrapped_data_from_database(master_product_id)
    generated_content_using_LLM = utils.generate_prompt_based_on_market_data(get_scrapped_data["content"], market_settings, master_product_id, selected_market_id)
    return generated_content_using_LLM

def generate_content_local(local_master_id):
    
    prompt_obj = utils.get_prompt_from_database(local_master_id)
    prompt= prompt_obj["prompt"]
    
    # prompt = response["prompt"]
    try:
        if settings.AI_SERVICE == "OPEN_AI":
            response = ai_service_obj.openai_response(prompt)
        elif settings.AI_SERVICE == "AZURE_LLM":
            pass
        return response
    except Exception as e:
        print("Error:", e)
        return None    

def get_list_of_local_products(master_product_id:int):
    return utils.local_products_list(master_product_id)

def get_one_local_master(id:int):
    return utils.get_one_local_master_from_database(id)