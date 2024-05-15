from core.apps.distributor_market_managment import utils
from openai import OpenAI

from core.config import settings
from openai import OpenAI

client = OpenAI(api_key = settings.OPENAI_API_KEY)


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


def distributor_version_content_generator(distributorVersion_id):
    prompt_obj = utils.get_prompt_from_database(distributorVersion_id)
    prompt= prompt_obj["prompt"]
    
    # prompt = response["prompt"]
    try:
        response_obj = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can choose other engines as well
            # messages=[{"role": "system", "content":prompt}],
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Generate content based on the product details and distributor details ."}
            ]
        )
        response = response_obj.choices[0].message.content
        utils.insert_generated_content_database(response, distributorVersion_id)

        return response
    except Exception as e:
        print("Error:", e)
        return None    


