import streamlit as st
import json
from components import sidebar
from middleware.product_service import fetch_product
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, hr, createBtn
from middleware.market_service import fetch_all_markets
from middleware.distributor_service import fetch_all_distributors
from middleware.product_service import fetch_all_products

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

json_data = ""

with home_container:
    main_card = generate_main_card()
    markets = fetch_all_markets()
    distributors = fetch_all_distributors()
    products = fetch_all_products()

    with main_card:
        if markets:
            centered_text("Here is a list of all markets:", "black", direction='left', size=20, bold='bold')
            with st.expander("Show"):
                # Convert the list of market dictionaries to a JSON formatted string
                markets_str = json.dumps(markets, indent=4)
                # Display the editable text area
                edited_markets_str = st.text_area("Editable Markets", value=markets_str, height=200)
                # Convert the edited string back to a list of dictionaries
                try:
                    edited_markets = json.loads(edited_markets_str)
                    st.write("You have edited the markets to:")
                    st.write(edited_markets)
                except json.JSONDecodeError:
                    st.error("The edited markets are not valid JSON.")
            col1, col2, col3 = st.columns([4, 4, 4])
            with col2:
                # Call the save markets function
                if st.button("Save markets", type="primary"):
                   st.write('saved')

        else:
            st.warning("No markets available.")

        if distributors:
            centered_text("Here is a list of all distributors:", "black", direction='left', size=20, bold='bold')
            with st.expander("Show"):
                # Convert the list of distributors dictionaries to a JSON formatted string
                distributors_str = json.dumps(distributors, indent=4)
                # Display the editable text area
                edited_distributors_str = st.text_area("Editable distributors", value=distributors_str, height=200)
                # Convert the edited string back to a list of dictionaries
                try:
                    edited_distributors = json.loads(edited_distributors_str)
                    st.write("You have edited the distributors to:")
                    st.write(edited_distributors)
                except json.JSONDecodeError:
                    st.error("The edited distributors are not valid JSON.")
            col1, col2, col3 = st.columns([4, 4, 4])
            with col2:
                # Call the save markets function
                if st.button("Save distributors", type="primary"):
                   st.write('saved')

        else:
            st.warning("No distributors available.")


        if products:
            centered_text("Here is a list of all products:", "black", direction='left', size=20, bold='bold')
            with st.expander("Show"):
                # Convert the list of products dictionaries to a JSON formatted string
                products_str = json.dumps(products, indent=4)
                # Display the editable text area
                edited_products_str = st.text_area("Editable products", value=products_str, height=200)
                # Convert the edited string back to a list of products
                try:
                    edited_products = json.loads(edited_products_str)
                    st.write("You have edited the products to:")
                    st.write(edited_products)
                except json.JSONDecodeError:
                    st.error("The edited products are not valid JSON.")
            col1, col2, col3 = st.columns([4, 4, 4])
            with col2:
                # Call the save products function
                if st.button("Save products", type="primary"):
                   st.write('saved')

        else:
            st.warning("No products available.")

