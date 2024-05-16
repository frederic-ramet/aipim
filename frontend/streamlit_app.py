import streamlit as st
import pandas as pd
from components.products import display_products
from fake import masterProducts
from middleware.product_service import fetch_all_products


# Function to generate a styled clickable link
def generate_clickable_text(text):
    return f'<a href="{text}" title="view more">view more</a>'  # Replace "#" with actual URL if needed


st.set_page_config(page_title="AI PIM Backoffice", layout="wide")

from components import sidebar
from utils.style import generate_main_container, generate_top_container, generate_main_card  # Modified import

sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

with home_container:
    right_actions = [{
        "text": "Add master product",
        "key": "add-product",
        "page": "addProduct",
        "type": "primary",  # "secondary" or "primary"
    }]
    main_card = generate_main_card("Products", right_actions)

    # Selecting specific columns from masterProducts
    selected_columns = ["title", "url", "description", "created_at", "id"]
    fake_data_df = pd.DataFrame(masterProducts)[selected_columns]

    with main_card:
        st.text('Here is a list of already optimized products (MASTER PRODUCT):')
        display_products(masterProducts, True)
        #products = fetch_all_products()
        #if len(products)>0:
         #   display_products(products, True)
        #else:
         #   st.warning("No products")
