from core.apps.master_product_managment import utils
import json
from openai import OpenAI

from core.config import settings
client = OpenAI(api_key = settings.OPENAI_API_KEY)


def list_master_products():
    response = utils.get_master_product_info()
    return response

def scrap_content_form_url(product_url:str):
    response = utils.get_product_from_nexans_website(product_url)
    print(response)
    utils.app_product_to_database(eval(response))
    return response