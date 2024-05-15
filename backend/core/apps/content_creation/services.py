from core.apps.content_creation import utils
from openai import OpenAI

from core.config import settings
client = OpenAI(api_key = settings.OPENAI_API_KEY)

def generate_prompt_local(master_product_id:int, selected_market_id:int, market_settings:str):
    get_scrapped_data = utils.get_scrapped_data_from_database(master_product_id)
    
    generated_content_using_LLM = utils.generate_prompt_based_on_market_data(get_scrapped_data["content"], market_settings, master_product_id, selected_market_id)
    return generated_content_using_LLM

def generate_content_local(local_master_id):
    
    prompt_obj = utils.get_prompt_from_database(local_master_id)
    prompt= prompt_obj["prompt"]
    
    # prompt = response["prompt"]
    try:
        response_obj = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can choose other engines as well
            # messages=[{"role": "system", "content":prompt}],
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Generate content based on the given details."}
            ]
        )
        response = response_obj.choices[0].message.content
        utils.insert_generated_content_database(response, local_master_id)

        return response
    except Exception as e:
        print("Error:", e)
        return None    

def get_list_of_local_products(master_product_id:int):
    return utils.local_products_list(master_product_id)

def get_one_local_master(id:int):
    return utils.get_one_local_master_from_database(id)