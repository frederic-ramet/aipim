import requests
import streamlit as st

base_url = st.secrets['BACKEND_BASE_URL']


# Function to fetch product
def fetch_product(product_url_input):
    scrap_product_url = f"{base_url}/api/v1/scrap_data?product_url={product_url_input}"
    try:
        response = requests.get(scrap_product_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all user apps data: {e}")
        return {}


def fetch_all_products():
    scrap_product_url = f"{base_url}/api/v1/list_master_products"
    try:
        response = requests.get(scrap_product_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all user apps data: {e}")
        return {}
