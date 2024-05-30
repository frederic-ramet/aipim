import streamlit as st
from components import sidebar
from middleware.local_master_service import fetch_local_master_by_id
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, \
    container_with_border, createBtn

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")

home_container = generate_main_container()

with home_container:
    if not st.session_state:
        main_card = generate_main_card("Generation session expired")
        with main_card:
            st.write("Session data is missing. Please navigate back.")
            createBtn("/", 'back')
    if 'local_master_id' in st.session_state:
        local_master_id = st.session_state['local_master_id']
        product_id = st.session_state['product_id']
        final_content = st.session_state['distributor_version_content']
        selected_distributor_label = st.session_state['selected_distributor']
        local_master = fetch_local_master_by_id(local_master_id)
        main_card = generate_main_card(f"New DISTRIBUTOR VERSION for Product reference: {local_master['title']} | {local_master['marketName']} | {selected_distributor_label}")

        with main_card:
            if local_master:
                centered_text('DISTRIBUTOR VERSION’s content', 'black', 'left', 18, 'bold')
                custom_css = "background-color: #FFF5F5;"
                second_card = container_with_border(custom_css)
                with second_card:
                    st.write('Here’s go the content of the generated DISTRIBUTOR VERSION ...')
                    st.markdown(f"<pre>{final_content}</pre>", unsafe_allow_html=True)
                col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 2, 2, 2, 2, 2, 1])

                with col2:
                    createBtn(f"localMasterPage?id={local_master_id}&product_id={product_id}", "Back")

                with col3:
                    createBtn(f"newDistributorVersion?local_master_id={local_master_id}&product_id={product_id}",
                              "Edit")  # todo reload modified market settings

                with col4:
                    downloaded_file = st.download_button(
                        label="Download as TXT",
                        data=final_content,
                        file_name=f"{local_master['title'].replace(' ', '_')}.txt",
                        mime="application/txt",
                        type="primary",
                    )
                with col5:
                    if st.button("Download as Doc", type="primary"):
                        st.warning('soon', icon="⚠️")
                with col6:
                    if st.button("Download as PDF", type="primary"):
                        st.warning('soon', icon="⚠️")
