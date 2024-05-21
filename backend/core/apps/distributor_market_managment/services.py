from core.apps.distributor_market_managment import utils
from core.config import settings
from core import utils as core_utils

ai_service_obj = core_utils.aiService()

def list_markets():
    query = "SELECT * FROM market"
    response = utils.get_list_from_database(query)
    return response

def list_distributors():
    query = "SELECT * FROM distributor"
    response = utils.get_list_from_database(query)
    return response

def distributor_prompt_generator(distributor_id:int, local_master_id:int, distributor_settings:str):
    
    distributor_query = "SELECT * FROM distributor WHERE id = ?"
    distributor_params = (distributor_id,)
    distributor_info_from_database = utils.get_specific_info_from_database(distributor_query, distributor_params)
    
    localMaster_query = "SELECT * FROM localMaster WHERE id = ?"
    localMaster_params = (local_master_id,)
    localMaster_info_from_database = utils.get_specific_info_from_database(localMaster_query, localMaster_params)
    
    response = utils.distributor_prompt_generator(distributor_info_from_database, localMaster_info_from_database, distributor_settings)
    return response


def distributor_version_content_generator(distributor_id, local_master_id, distributor_settings,  prompt):
    # prompt_obj = utils.get_prompt_from_database(prompt)
    # prompt = prompt_obj["prompt"]
    # prompt = response["prompt"]
    
    try:
        if settings.AI_SERVICE == "OPEN_AI":
            response = ai_service_obj.openai_response(prompt)
        elif settings.AI_SERVICE == "AZURE_LLM":
            pass
        

        distributor_query = "SELECT * FROM distributor WHERE id = ?"
        distributor_params = (distributor_id,)
        distributor_info_from_database = utils.get_specific_info_from_database(distributor_query, distributor_params)
        
        localMaster_query = "SELECT * FROM localMaster WHERE id = ?"
        localMaster_params = (local_master_id,)
        localMaster_info_from_database = utils.get_specific_info_from_database(localMaster_query, localMaster_params)
        
        distributorVersion_title = f"{distributor_info_from_database['label']}_{distributor_info_from_database['format']}"
        distributorVersion_distributor = f"{distributor_info_from_database['label']}"
        distributorVersion_distributorId = f"{distributor_info_from_database['id']}"
        distributorVersion_settings = distributor_settings
        distributorVersion_prompt = prompt
        distributorVersion_content = f"{localMaster_info_from_database["content"]}"
        distributorVersion_localMasterId = f"{localMaster_info_from_database['id']}"

        utils.insert_info_to_database(distributorVersion_title, distributorVersion_distributor, distributorVersion_distributorId, distributorVersion_settings, distributorVersion_prompt, distributorVersion_content, distributorVersion_localMasterId)

        return response
    except Exception as e:
        print("Error:", e)
        return None


