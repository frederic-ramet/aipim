import requests
import streamlit as st

base_url = st.secrets['BACKEND_BASE_URL']


# Function to fetch markets
def fetch_all_distributors():
    scrap_distributor_url = f"{base_url}/api/v1/list_distributors"
    try:
        response = requests.get(scrap_distributor_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all distributors data: {e}")
        return []


def generate_prompt_distributor(distributor_id, local_master_id, settings):
    generated_prompt_url = f"{base_url}/api/v1/distributor_prompt_generator"
    generated_prompt_url = f"{generated_prompt_url}?distributor_id={distributor_id}"
    generated_prompt_url = f"{generated_prompt_url}&local_master_id={local_master_id}"
    generated_prompt_url = f"{generated_prompt_url}&distributor_settings={settings}"

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


def generate_distributor_version(distributor_id, local_master_id, distributor_settings, prompt):
    generated_content_url = f"{base_url}/api/v1/distributor_version_content_generator"
    generated_content_url = f"{generated_content_url}?distributor_id={distributor_id}"
    generated_content_url = f"{generated_content_url}&local_master_id={local_master_id}"
    generated_content_url = f"{generated_content_url}&distributor_settings={distributor_settings}"
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
