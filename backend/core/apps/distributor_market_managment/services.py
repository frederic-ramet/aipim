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


def get_one_distributor_version(id):
    return utils.get_one_distributor_version_from_database(id)


def distributor_prompt_generator(distributor_id: int, local_master_id: int, distributor_settings: str):
    distributor_info_from_database = utils.get_distributor_info(distributor_id)
    localMaster_info_from_database = utils.get_localmaster_info(local_master_id)

    response = utils.distributor_prompt_generator(distributor_info_from_database, localMaster_info_from_database,
                                                  distributor_settings)
    return response


def distributor_version_content_generator(distributor_id, local_master_id, distributor_settings, prompt):
    try:
        if settings.AI_SERVICE == "OPEN_AI":
            distribution_content = ai_service_obj.openai_response(prompt)
        elif settings.AI_SERVICE == "AZURE_LLM":
            pass

        distributor_info_from_database = utils.get_distributor_info(distributor_id)
        localMaster_info_from_database = utils.get_localmaster_info(local_master_id)

        # create_seo_optimized_prompt = utils.create_seo_optimized_prompt(distributor_info_from_database["seoKeywords"], distribution_content)

        # if settings.AI_SERVICE == "OPEN_AI":
        #     seo_optimized_content = ai_service_obj.openai_response(create_seo_optimized_prompt)
        # elif settings.AI_SERVICE == "AZURE_LLM":
        #     pass

        distributorVersion_title = f"{distributor_info_from_database['label']}_{distributor_info_from_database['target']}"
        distributorVersion_distributor = f"{distributor_info_from_database['label']}"
        distributorVersion_distributorId = f"{distributor_info_from_database['id']}"
        distributorVersion_settings = distributor_settings
        distributorVersion_prompt = prompt
        distributorVersion_content = distribution_content
        distributorVersion_localMasterId = f"{localMaster_info_from_database['id']}"

        utils.insert_info_to_database(distributorVersion_title, distributorVersion_distributor,
                                      distributorVersion_distributorId, distributorVersion_settings,
                                      distributorVersion_prompt, distributorVersion_content,
                                      distributorVersion_localMasterId)

        distributor_content_response = {
            "title": distributorVersion_title,
            "distributor": distributorVersion_distributor,
            "content": distributorVersion_content,
            "seo_keywords": distributor_info_from_database["seoKeywords"]
        }
        return distribution_content
    except Exception as e:
        print("Error:", e)
        return None


def get_list_of_distributer_versions(local_master_id: int):
    return utils.distributer_versions_list(local_master_id)
