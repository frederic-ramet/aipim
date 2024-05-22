import streamlit as st
import json
from components import sidebar
from middleware.local_master_service import generate_local_product, fetch_local_master_by_id
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, \
    container_with_border
from utils.utils import parse_settings

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")

params = st.experimental_get_query_params()
local_master_id = params.get('id', [None])[0]
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM ")
home_container = generate_main_container()

with home_container:
    local_master = fetch_local_master_by_id(local_master_id)
    if local_master:
        main_card = generate_main_card('LOCAL MASTER for: ' + local_master['title'])
        with main_card:
            centered_text('Applied settings:', 'black', 'left', 18)
            custom_css = "background-color: #FFF5F5;"
            second_card = container_with_border(custom_css)
            with second_card:
                settings = local_master.get('settings')
                if settings:
                    # Fix for trailing commas: Remove any trailing commas from the settings string
                    settings = settings.rstrip(',')  # Remove trailing commas (optional)

                    # Debug print to inspect the settings string
                    st.write("Settings string:")
                    st.write(settings)
                    print("Settings string:", settings)
                    settings = settings.replace("\n", "")
                    settings = settings.replace('\"', '"')
                    settings = settings.replace("'", '"')
                    settings = "{" + settings + "}"
                    # Try parsing the JSON string
                    try:
                        settings_obj = json.loads(settings)
                        st.write("Parsed settings object:")
                        st.write(settings_obj)
                        st.write(settings_obj['marketFeatures'])
                    except json.JSONDecodeError as e:
                        st.error(f"Error parsing settings JSON: {e}")
                        print(f"Error parsing settings JSON: {e}")
                else:
                    st.warning("No settings available for this local master.")
    else:
        st.error("Local master not found.")