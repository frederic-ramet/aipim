import pandas as pd
import streamlit as st
from components import sidebar
from fake import local_master
from components.products import display_products, display_product
from middleware.product_service import fetch_master_product_by_id, fetch_master_product_by_id_fake,show_json
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, hr
from utils.utils import is_valid_url

params = st.query_params.to_dict()
product_id = params['id']

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

json_data = ""

with home_container:
    main_card = generate_main_card('MASTER PRODUCT Page: ')
    with main_card:
        st.text("Here are all product’s informations.")
        master_product = fetch_master_product_by_id_fake(product_id)

        if master_product:
            left, right = st.columns([1, 4])
            with left:
                centered_text('Product Name:', 'black', 'left', 18, 'bold')
                centered_text('Product URL:', 'black', 'left', 18, 'bold')
                centered_text('Product JSON:', 'black', 'left', 18, 'bold')
            with right:
                centered_text(str(master_product['title']), 'black', 'left', 18, '')
                st.markdown(f"[{master_product['url']}]({master_product['url']})")
                st.markdown(
                    f'<div style="text-align: left; font-size: 18px; font-weight: bold; color: black;"><a href="javascript:void(0);'
                    f'" onclick="show_json();">Show</a>:<a href="hello">Download</a></div>',
                    unsafe_allow_html=True)
        centered_text('Generated Contents (LOCAL MASTER):', 'black', 'left', 18, 'bold')
        selected_columns = ["title", "url", "content_params"]
        display_product(local_master)

