import requests
import streamlit as st

base_url = st.secrets['BACKEND_BASE_URL']


# Function to fetch markets
def fetch_all_markets():
    scrap_market_url = f"{base_url}/api/v1/list_markets"
    try:
        response = requests.get(scrap_market_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all markets data: {e}")
        return []


def generate_prompt(master_product_id, selected_market_id, market_settings):
    generated_prompt_url = f"{base_url}/api/v1/generate_prompt"
    generated_prompt_url = f"{generated_prompt_url}?master_product_id={master_product_id}"
    generated_prompt_url = f"{generated_prompt_url}&selected_market_id={selected_market_id}"
    generated_prompt_url = f"{generated_prompt_url}&market_settings={market_settings}"

    try:
        response = requests.post(generated_prompt_url, json={})
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

