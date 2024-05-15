import streamlit as st
import pandas as pd
from components.dfTable import build_table
from fake import fake_data

# Function to generate a styled clickable link
def generate_clickable_text(text):
  return f'<a href="#" title="view more">{text}</a>'  # Replace "#" with actual URL if needed

st.set_page_config(page_title="AI PIM Backoffice", layout="wide")

from components import sidebar
from utils.style import generate_main_container, generate_top_container, centered_text, generate_main_card

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
    fake_data_df = pd.DataFrame(fake_data)
    # Add a new column named "View More" with clickable text
    fake_data_df["View More"] = fake_data_df["url"].apply(
        generate_clickable_text)  # Replace "url" with actual column name if different

    with main_card:
        st.text('Here is a list of already optimized products (MASTER PRODUCT):')

        # Call build_table with the modified DataFrame
        build_table(fake_data_df, {}, True)
