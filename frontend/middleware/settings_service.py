import requests
import streamlit as st

from middleware.utility import post_to_backend

base_url = st.secrets['BACKEND_BASE_URL']


def update_markets(settings):
    url = f"{base_url}/api/v1/update_market_json_file"
    url = f"{url}?json_data={settings}"
    return post_to_backend(url, {})


def update_distributors(settings):
    url = f"{base_url}/api/v1/update_distributors_json_file"
    url = f"{url}?json_data={settings}"
    return post_to_backend(url, {})


def update_features(settings):
    url = f"{base_url}/api/v1/update_features_json_file"
    url = f"{url}?json_data={settings}"
    return post_to_backend(url, {})


def update_marketing_axis(settings):
    url = f"{base_url}/api/v1/update_marketing_axis_json_file"
    url = f"{url}?json_data={settings}"
    return post_to_backend(url, {})


def get_full_settings():
    back_url = f"{base_url}/api/v1/get_all_data"
    try:
        response = requests.get(back_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all settings data: {e}")
        return []
