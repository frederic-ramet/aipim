from components import sidebar
from utils.style import generate_main_container, generate_top_container, generate_main_card
import streamlit as st

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Add new Product")
home_container = generate_main_container()

with home_container:
    right_actions = [{
        "text": "Fetch product",
        "key": "back-user",
        "page": "users_page",
        "type": "primary",  # "secondary" or "primary"
    }]
    main_card = generate_main_card('Add MASTER PRODUCT', right_actions)
    with main_card:
        st.title("Add new product")
        st.text("Add new Product")
        # Form fields for adding a new user
        product_url = st.text_input("Product URL")


            # Call the function to create user
            # create_user(user_data)
