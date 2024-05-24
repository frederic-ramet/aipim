import streamlit as st
import json
from components import sidebar
from middleware.product_service import fetch_master_product_by_id
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, \
    container_with_border, createBtn

# Function to redirect to streamlit_app page
def redirect_to_streamlit_app():
    st.write("Session data is missing. Please navigate back to the home page.")

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()
# Check if session is empty, redirect to home page
if not st.session_state:
    redirect_to_streamlit_app()
with home_container:
    if 'local_generated_product_id' in st.session_state:
        product_id = st.session_state['local_generated_product_id']
        final_content = st.session_state['local_generated_content']
        master_product = fetch_master_product_by_id(product_id)
        main_card = generate_main_card('NEW LOCAL MASTER for: ' + master_product['title'])

        with main_card:
            if master_product:
                centered_text('Generated content for the Local Master', 'black', 'left', 18, 'bold')
                custom_css = "background-color: #FFF5F5;"
                second_card = container_with_border(custom_css)
                with second_card:
                    st.write('Here’s go the content of the generated LOCAL Master ...')
                    st.markdown(f"<pre>{final_content}</pre>", unsafe_allow_html=True)
                col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 2, 2, 2, 1])
                with col2:
                    createBtn(f"newLocalMaster1?id={product_id}", "Back")  # todo reload modified market settings

                with col3:
                    # Convert dictionary to JSON string
                    final_content_json = json.dumps(final_content)
                    # Encode JSON string to bytes
                    final_content_bytes = final_content_json.encode('utf-8')
                    downloaded_file = st.download_button(
                        label="Download as TXT",
                        data=final_content_bytes,
                        file_name=f"{master_product['title'].replace(' ', '_')}.txt",
                        mime="application/txt",
                        type="primary",
                    )
                with col4:
                    if st.button("Download as Doc", type="primary"):
                        st.warning('soon', icon="⚠️")
                with col5:
                    if st.button("Download as PDF", type="primary"):
                        st.warning('soon', icon="⚠️")
