from core.apps.content_creation import utils
def scrap_content_form_url(product_url:str):
    response = utils.get_product_from_nexans_website(product_url)
    print(response)
    return response