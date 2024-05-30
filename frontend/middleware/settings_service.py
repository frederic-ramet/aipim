import requests
import streamlit as st

base_url = st.secrets['BACKEND_BASE_URL']


def update_markets(markets_settings):
    url = f"{base_url}/api/v1/update_features_json_file"
    url = f"{url}?json_data={markets_settings}"

    try:
        response = requests.post(url, json={})
        response = response.json()
        if 'error' in response:
            st.error(response.get('error'))
            return None
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
        if http_err.response.status_code == 422:
            st.error(f"Response content: {http_err.response.text}")
        return None
    except requests.exceptions.RequestException as req_err:
        st.error(f"Request error occurred: {req_err}")
        return None


def get_full_settings():
    back_url = f"{base_url}/api/v1/get_all_data"
    try:
        response = requests.get(back_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all settings data: {e}")
        return []
