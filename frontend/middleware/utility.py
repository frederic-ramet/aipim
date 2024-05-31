import requests
import streamlit as st


def post_to_backend(url: str, json=None):
    if json is None:
        json = {}

    try:
        response = requests.post(url, json)
        response_data = response.json()
        if 'error' in response:
            st.error(response_data.get('error'))
            return None
        response.raise_for_status()
        return response_data
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
        if http_err.response.status_code == 422:
            st.error(f"Response content: {http_err.response.text}")
        return None
    except requests.exceptions.RequestException as req_err:
        st.error(f"Request error occurred: {req_err}")
        return None
