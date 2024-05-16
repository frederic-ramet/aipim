import requests
import streamlit as st
import json
from fake import product, masterProducts

base_url = st.secrets['BACKEND_BASE_URL']


# Function to fetch product
def fetch_product(product_url_input):
    return json.dumps(product, indent=4)
    #scrap_product_url = f"{base_url}/api/v1/scrap_data?product_url={product_url_input}"
    #try:
    #   response = requests.get(scrap_product_url)
    #   response.raise_for_status()
    #   return response.json()
    #except requests.exceptions.RequestException as e:
    #   st.error(f"Error fetching all user apps data: {e}")
    #   return {}


def fetch_all_products():
    return ""
    #scrap_product_url = f"{base_url}/api/v1/list_master_products"
    #try:
    #   response = requests.get(scrap_product_url)
    #   response.raise_for_status()
    #   return response.json()
    #except requests.exceptions.RequestException as e:
    #    st.error(f"Error fetching all user apps data: {e}")
    #    return []

def fetch_master_product_by_id(product_id):
    get_product_product_api_url = f"{base_url}/api/v1/product/profile/{product_id}"

   # access_token = get_access_token()
   # headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(get_product_product_api_url)
        response.raise_for_status()
        product_result = response.json().get("data")
        st.write("product_result: ")
        st.write(product_result)
        return product_result
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching product information by id: {e}")


def fetch_master_product_by_id_fake(product_id):
    try:
        # Ensure product_id is an integer
        product_id = int(product_id)

        # Search for the product by its ID in the masterProducts list
        product = next((p for p in masterProducts if p["id"] == product_id), None)

        if product:
            return product
        else:
            st.error(f"Product with ID {product_id} not found")
    except Exception as e:
        st.error(f"Error fetching product information by id: {e}")


def show_json():
    return "Hello"