from core.apps.content_creation import utils
from core import utils as core_utils
from core.apps.content_creation.utils import store_info_in_to_database, get_market_info
from core.config import settings
from bs4 import BeautifulSoup


ai_service_obj = core_utils.aiService()


def generate_prompt_local(master_product_id: int, selected_market_id: int, market_settings: str):
    get_scrapped_data = utils.get_scrapped_data_from_database(master_product_id)
    generated_content_using_LLM = utils.generate_prompt_based_on_market_data(get_scrapped_data["content"],
                                                                             selected_market_id,
                                                                             market_settings)
    return generated_content_using_LLM


def generate_content_local(master_product_id: int, selected_market_id: int, market_settings: str, prompt: str):
    market_info_from_database = get_market_info(selected_market_id)
    try:

        generated_content = ""
        get_scrapped_data = utils.get_scrapped_data_from_database(master_product_id)
        scrapped_data_dict = eval(get_scrapped_data["content"])
        


        if settings.AI_SERVICE == "OPEN_AI":
            generated_content = ai_service_obj.openai_response(prompt)
            soup = BeautifulSoup(generated_content, 'html.parser')
            generated_title = soup.find('h1').get_text()
            print("^^ ^^ " * 20)
            print("^^ ^^ " * 20)
            print(generated_title)
            print("^^ ^^ " * 20)
            print("^^ ^^ " * 20)
            
            store_info_in_to_database(prompt, market_settings, master_product_id, selected_market_id,
                                      market_info_from_database, generated_content, scrapped_data_dict, generated_title)

        elif settings.AI_SERVICE == "AZURE_LLM":
            pass

        response_dict = {
            "title": scrapped_data_dict["title"],
            "description": scrapped_data_dict["description"],
            "content": generated_content
        }

        return response_dict
    except Exception as e:
        print("Error:", e)
        return None


def get_list_of_local_products(master_product_id: int):
    return utils.local_products_list(master_product_id)


def get_one_local_master(id: int):
    return utils.get_one_local_master_from_database(id)
