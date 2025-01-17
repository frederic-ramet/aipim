import streamlit as st
from components import sidebar
from components.localMaster import display_local_master_list
from middleware.local_master_service import fetch_local_products, delete
from middleware.product_service import fetch_master_product_by_id, fetch_product
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text,createBtn

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")

params = st.query_params.to_dict()
product_id = params['id']

sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

with home_container:
    master_product = fetch_master_product_by_id(product_id)
    main_card = generate_main_card('Product reference: '+ master_product['title'])
    with main_card:
        st.text("Here are all product’s informations.")
        json_data = master_product['content']
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
                    file_name=f"{master_product['title'].replace(' ','_')}.json",
                    mime="application/json",
                    type="primary",
                )
        st.write('')
        centered_text('Generated Contents (LOCAL MASTER):', 'black', 'left', 18, 'bold')
        st.write('')
        local_products = fetch_local_products(product_id)
        if 'delete_local_product' in params:
            delete_local_product = params['delete_local_product']
            done = delete(delete_local_product)
            if done:
                st.toast('Deleted!', icon='🎉')
                local_products = fetch_local_products(product_id)
        if local_products:
            display_local_master_list(product_id, local_products, True)
            st.write('')
        col1, col2, col3 = st.columns([4, 4, 4])
        with col2:
            createBtn(f"newLocalMaster1?id={product_id}", "Generate new Local Master")
            st.write('')

