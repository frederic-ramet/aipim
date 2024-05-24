import streamlit as st
from components import sidebar
from middleware.local_master_service import fetch_local_master_by_id
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, \
    container_with_border, createBtn
from utils.utils import parse_market_settings

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")

params = st.query_params.to_dict()
local_master_id = params['id']
product_id = params['product_id']

sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM ")
home_container = generate_main_container()

with home_container:
    local_master = fetch_local_master_by_id(local_master_id)
    main_card = generate_main_card('LOCAL MASTER for: ' + local_master['title'])
    with main_card:
        if local_master:
            left, right = st.columns([1, 10])
            with left:
                centered_text('Selected market', 'black', 'left', 18, 'bold')
                centered_text('Applied settings:', 'black', 'left', 18)
            with right:
                st.write(local_master.get('marketName'))
                custom_css = "background-color: #FFF5F5;"
                second_card = container_with_border(custom_css)
                with second_card:
                    settings = local_master.get('settings')
                    if settings:
                        settings_obj = parse_market_settings(settings)
                        st.write(settings_obj)
                    else:
                        st.warning("No settings available for this local master.")

            centered_text('Used Prompt', 'black', 'left', 18, 'bold')
            custom_css = "background-color: #FFF5F5;"
            prompt_card = container_with_border(custom_css)
            with prompt_card:
                st.write(local_master.get('prompt'))

            centered_text('Generated content', 'black', 'left', 18, 'bold')
            custom_css = "background-color: #FFF5F5;"
            prompt_card = container_with_border(custom_css)
            with prompt_card:
                st.write(local_master.get('content'))
        else:
            st.error("Local master not found.")
        col1, col2, col3, col4 = st.columns([2, 4, 4, 2])
        with col2:
            createBtn(f'/masterProductPage?id={product_id}', 'Back')
        with col3:
            createBtn(f'/newDistributorVersion?local_master_id={local_master_id}&product_id={product_id}', 'Generate DISTRIBUTOR VERSION')


