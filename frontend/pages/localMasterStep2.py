import streamlit as st
from components import sidebar
from components.products import display_local_master_list
from middleware.market_service import fetch_all_markets, generate_prompt_test
from middleware.product_service import fetch_master_product_by_id, fetch_product
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, hr, \
    generate_card, container_with_border

params = st.query_params.to_dict()
product_id = 1  #;params['id']
st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

with home_container:
    master_product = fetch_master_product_by_id(product_id)
    main_card = generate_main_card('NEW LOCAL MASTER for: ' + master_product['title'])
    markets = fetch_all_markets()
    # Extract titles from the list of market dictionaries
    market_titles = [market['title'] for market in markets]

    with main_card:
        if master_product:
            centered_text('Step2 (Validation):  Please provide the next informations:', 'black', 'left', 18, 'bold')
            centered_text('LOCAL Master’s content', 'black', 'left', 18, 'bold')
            custom_css = "background-color: #FFF5F5;"
            second_card = container_with_border(custom_css)
            with second_card:
                st.write('Here’s go the content of the generated LOCAL Master ...')
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1])
        with col2:
            if st.button("<= go back", type="primary"):
                st.switch_page("localMaster.py")
        with col3:
            if st.button("Save", type="primary"):
                st.switch_page("localMaster.py")

        with col4:
            if st.button("Download as TXT", type="primary"):
                st.switch_page("localMaster.py")
        with col5:
            if st.button("Download as Doc", type="primary"):
                st.switch_page("localMaster.py")
        with col6:
            if st.button("Download as PDF", type="primary"):
                st.switch_page("localMaster.py")
