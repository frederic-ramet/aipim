import streamlit as st
from components import sidebar
from components.localMaster import display_local_master_list
from middleware.local_master_service import fetch_local_products
from middleware.product_service import fetch_master_product_by_id, fetch_product
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text,createBtn

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")

params = st.query_params.to_dict()
distributor_version_id = params['id']
local_master_id = params['local_master_id']
product_id = params['product_id']

sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

with home_container:
    #master_product = fetch_master_product_by_id(product_id)
    main_card = generate_main_card('Distributor Version: ')
    with main_card:
        st.text("Here are all distributor’s information.")
