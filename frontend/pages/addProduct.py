import streamlit as st
from components import sidebar
from middleware.product_service import fetch_product
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, hr
from utils.utils import is_valid_url

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

json_data = ""

with home_container:
    main_card = generate_main_card('Add MASTER PRODUCT')
    with main_card:
        st.text("Add a product by importing it from Nexans website.")
        centered_text("Product URL:", "black", direction='left', size=20, bold='bold')
        col1, col2 = st.columns([20, 1])
        with col1:
            product_url = st.text_input("", placeholder="Product URL")
            url_is_not_valid = product_url != '' and not is_valid_url(product_url)
            if url_is_not_valid:
                st.warning('Please enter a valid URL')

        col11, col22 = st.columns([5, 1])
        with col22:
            # Call the fetch_product function directly with the text input element
            if st.button("Fetch product", type="primary", disabled=url_is_not_valid):
                json_data = fetch_product(product_url)  # Pass the element directly

        hr()
        centered_text("Imported Product", "black", direction='left', size=20, bold='bold')

        col13, col23 = st.columns([20, 1])
        with col13:
            # Display the value of text_area_value
            text_area_value = st.text_area("", value=json_data, height=250, disabled=True)

        # Add the three primary buttons centered on the page
        col14, col24, col34, col44, col54 = st.columns([2, 2, 2, 2, 2])
        with col24:
            if st.button("Import Product", type="primary", disabled=(text_area_value == '')):
                st.switch_page("streamlit_app.py")
        with col34:
            if st.button("Generate Content", type="primary", disabled=text_area_value == ''):
                # Functionality for generating content
                pass
        with col44:
            downloaded_file = st.download_button(
                label="Download JSON",
                data=json_data,
                file_name="data.json",
                mime="application/json",
                type="primary",
                disabled=text_area_value == ''
            )