import streamlit as st
from components import sidebar
from components.products import display_local_master_list
from middleware.product_service import fetch_master_product_by_id, fetch_product
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, hr

params = st.query_params.to_dict()
product_id = params['id']

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

with home_container:
    master_product = fetch_master_product_by_id(product_id)
    main_card = generate_main_card('MASTER PRODUCT Page: '+master_product['title'])
    with main_card:
        st.text("Here are all product’s informations.")
        json_data = '' #fetch_product(master_product['url'])
        if master_product:
            left, right = st.columns([1, 4])
            with left:
                centered_text('Product Name:', 'black', 'left', 18, 'bold')
                centered_text('Product URL:', 'black', 'left', 18, 'bold')
                centered_text('Product JSON:', 'black', 'left', 18, 'bold')
            with right:
                centered_text(str(master_product['title']), 'black', 'left', 18, '')
                st.markdown(f"[{master_product['url']}]({master_product['url']})")
                downloaded_file = st.download_button(
                    label="Download JSON",
                    data=json_data,
                    file_name="data.json",
                    mime="application/json",
                    type="primary",
                )
        st.write('')
        centered_text('Generated Contents (LOCAL MASTER):', 'black', 'left', 18, 'bold')
        st.write('')
        local_products = fetch_master_product_by_id(product_id)
        display_local_master_list(local_products)
        col1, col2, col3 = st.columns([4, 2, 4])
        with col2:
            if st.button("Generate new content", type="primary"):
                st.switch_page("pages/localMaster.py")

