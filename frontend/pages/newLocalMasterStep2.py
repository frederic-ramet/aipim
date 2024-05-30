import streamlit as st
import json
from components import sidebar
from middleware.product_service import fetch_master_product_by_id
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, createBtn, \
    container_with_colored_bg

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

with home_container:
    # Check if session is empty, redirect to home page
    if not st.session_state:
        main_card = generate_main_card("Generation session expired")
        with main_card:
            st.write("Session data is missing. Please navigate back.")
            createBtn("/", 'back')
    if 'local_generated_product_id' in st.session_state:
        product_id = st.session_state['local_generated_product_id']
        final_content = st.session_state['local_generated_content']
        selected_market_title = st.session_state['local_generated_content_market']
        language = st.session_state['local_generated_content_lang']
        master_product = fetch_master_product_by_id(product_id)
        main_card = generate_main_card(
            f"LOCAL MASTER for: {master_product['title']} | {selected_market_title} | {language}")

        with main_card:
            if master_product:
                st.write('Title original')
                title_card = container_with_colored_bg()
                with title_card:
                    st.markdown(f"{final_content['title']}", unsafe_allow_html=True)

                st.write('Description original')
                desc_card = container_with_colored_bg()
                with desc_card:
                    st.markdown(f"{final_content['description']}", unsafe_allow_html=True)

                centered_text('Generated content for the Local Master', 'black', 'left', 18, 'bold')
                st.write('')
                content_card = container_with_colored_bg()
                with content_card:
                    st.markdown(f"<pre>{final_content['content']}</pre>", unsafe_allow_html=True)

                col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 2, 2, 2, 2, 2, 1])
                with col2:
                    createBtn(f"masterProductPage?id={product_id}", "Back")

                with col3:
                    createBtn(f"newLocalMaster1?id={product_id}", "Edit")  # todo reload modified market settings

                with col4:
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
                with col5:
                    if st.button("Download as Doc", type="primary"):
                        st.warning('soon', icon="⚠️")
                with col6:
                    if st.button("Download as PDF", type="primary"):
                        st.warning('soon', icon="⚠️")
