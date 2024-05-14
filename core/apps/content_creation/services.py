from core.apps.content_creation import utils
import json
from openai import OpenAI

from core.config import settings
client = OpenAI(api_key = settings.OPENAI_API_KEY)

def generate_prompt_local(scraped_data:str, selected_market:str):
    scraped_data_dict = json.loads(scraped_data)
    market_data = utils.get_market_info(selected_market)
    generated_content_using_LLM = utils.generate_prompt_based_on_market_data(scraped_data_dict, market_data)
    return generated_content_using_LLM

def generate_content_local(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can choose other engines as well
            # messages=[{"role": "system", "content":prompt}],
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Generate content based on the given details."}
            ]

        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        print("Error:", e)
        return None    
