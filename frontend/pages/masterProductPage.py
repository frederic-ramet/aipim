import streamlit as st
from components import sidebar
from middleware.product_service import fetch_product, save_product
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, hr
from utils.utils import is_valid_url

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

json_data = ""

with home_container:
    main_card = generate_main_card('MASTER PRODUCT Page: ')
    with main_card:
        st.text("Here are all product’s informations.")
        centered_text("Product Name:", "black", direction='left', size=20, bold='bold')
        centered_text("Product URL:", "black", direction='left', size=20, bold='bold')
        centered_text("Product JSON:", "black", direction='left', size=20, bold='bold')

        centered_text("Generated Contents (LOCAL MASTER):", "black", direction='left', size=20, bold='bold')




