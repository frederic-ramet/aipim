import json

import streamlit

from fake import product


# Function to fetch product
def fetch_product(product_url_input):
    # call backend to scrap this product
    return json.dumps(product, indent=4)


def save_product(product_url_input, json_data):
    # call backend to save product
    return ""
