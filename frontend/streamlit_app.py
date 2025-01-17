import streamlit as st
from components.products import display_products
from middleware.product_service import fetch_all_products, delete
import warnings
from components import sidebar
from utils.style import generate_main_container, generate_top_container, generate_main_card

warnings.filterwarnings("ignore", message="Could not infer format")

params = st.query_params.to_dict()

st.set_page_config(page_title="AI PIM Backoffice", layout="wide")

sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

with home_container:
    right_actions = [{
        "text": "Add a product reference",
        "key": "add-product",
        "page": "addProduct",
        "type": "primary",  # "secondary" or "primary"
    }]
    main_card = generate_main_card("Product references", right_actions)

    # Selecting specific columns from masterProducts
    selected_columns = ["title", "url", "description", "created_at", "id"]

    with main_card:
        st.text('Here is a list of already optimized products (MASTER PRODUCT):')
        products = fetch_all_products()
        if 'delete_master_product' in params:
            delete_master_product = params['delete_master_product']
            done = delete(delete_master_product)
            if done:
                st.toast('Deleted!', icon='🎉')
                products = fetch_all_products()
        if len(products) > 0:
            display_products(products, True)
            st.write('')
        else:
            st.warning("No products")
