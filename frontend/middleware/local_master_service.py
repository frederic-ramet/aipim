import requests
import streamlit as st
from fake import masterProducts

base_url = st.secrets['BACKEND_BASE_URL']


def fetch_local_master_by_id(local_master_id):
    get_master_product_api_url = f"{base_url}/api/v1/get_one_local_master?id={local_master_id}"

    try:
        response = requests.get(get_master_product_api_url)
        response.raise_for_status()
        local_master_result = response.json()
        return local_master_result
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching local master information by id: {e}")


def fetch_local_products(product_id):
    scrap_local_product_url = f"{base_url}/api/v1/list_local_products?master_product_id={product_id}"
    try:
        response = requests.get(scrap_local_product_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all local products data: {e}")
        return []


def generate_local_product(master_product_id, selected_market_id, market_settings, prompt):
    generated_content_url = f"{base_url}/api/v1/generate_content"
    generated_content_url = f"{generated_content_url}?master_product_id={master_product_id}"
    generated_content_url = f"{generated_content_url}&selected_market_id={selected_market_id}"
    generated_content_url = f"{generated_content_url}&market_settings={market_settings}"
    generated_content_url = f"{generated_content_url}&prompt={prompt}"

    try:
        response = requests.post(generated_content_url, json={})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
        if http_err.response.status_code == 422:
            st.error(f"Response content: {http_err.response.text}")
        return {}
    except requests.exceptions.RequestException as req_err:
        st.error(f"Request error occurred: {req_err}")
        return {}


def delete(delete_local_product):
    local_product_url = f"{base_url}/api/v1/delete_local_master_data?id={delete_local_product}"

    try:
        response = requests.delete(local_product_url)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting the local product information by id: {e}")
        return False
