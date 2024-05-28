import streamlit as st
from components import sidebar
from middleware.product_service import fetch_master_product_by_id, fetch_product
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, createBtn
from middleware.local_master_service import fetch_local_master_by_id
from middleware.distributor_service import fetch_distributor_version_by_id
from utils.utils import parse_market_settings

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")

params = st.query_params.to_dict()
distributor_version_id = params['id']
local_master_id = params['local_master_id']
product_id = params['product_id']

sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

with home_container:
    master_product = fetch_master_product_by_id(product_id)
    local_master = fetch_local_master_by_id(local_master_id)
    distributor_version = fetch_distributor_version_by_id(distributor_version_id)
    main_card = generate_main_card('Distributor Version for: ' + local_master['title'])
    with main_card:
        if distributor_version:
            centered_text(f"Distributor <i>{distributor_version.get('distributor')}</i>", 'black', 'left', 18, 'bold')
            centered_text(f"Local Master: {local_master.get('title')}", 'black', 'left', 18, 'bold')
            centered_text(f"Product: {master_product.get('title')}", 'black', 'left', 18, 'bold')

            st.write('')
            centered_text('Settings', 'black', 'left', 18, 'bold')
            with st.expander("Show"):
                settings = distributor_version.get('settings')
                if settings:
                    settings_obj = parse_market_settings(settings)
                    st.write(settings_obj)
                else:
                    st.warning("No settings available for this distributor version.")

            centered_text('Used Prompt', 'black', 'left', 18, 'bold')
            with st.expander("Show"):
                st.write(distributor_version.get('prompt'))


        else:
            st.error("Distributor version not found.")
        col1, col2, col3 = st.columns([4, 4, 4])
        with col2:
            createBtn(f'/localMasterPage?id={local_master_id}&product_id={product_id}', 'Back')
        st.write('')
