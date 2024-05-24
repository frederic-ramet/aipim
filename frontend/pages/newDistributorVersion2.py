import streamlit as st
from components import sidebar
from middleware.local_master_service import fetch_local_master_by_id
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, \
    container_with_border, createBtn

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
    if 'local_master_id' in st.session_state:
        local_master_id = st.session_state['local_master_id']
        product_id = st.session_state['product_id']
        final_content = st.session_state['distributor_version_content']
        local_master = fetch_local_master_by_id(local_master_id)
        main_card = generate_main_card('New DISTRIBUTOR VERSION  for: ' + local_master['title'])

        with main_card:
            if local_master:
                centered_text('DISTRIBUTOR VERSION’s content', 'black', 'left', 18, 'bold')
                custom_css = "background-color: #FFF5F5;"
                second_card = container_with_border(custom_css)
                with second_card:
                    st.write('Here’s go the content of the generated DISTRIBUTOR VERSION ...')
                    st.markdown(f"<pre>{final_content}</pre>", unsafe_allow_html=True)
                col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 2, 2, 2, 1])
                with col2:
                    createBtn(f"newDistributorVersion?local_master_id={local_master_id}&product_id={product_id}", "Back")  # todo reload modified market settings

                with col3:
                    downloaded_file = st.download_button(
                        label="Download as TXT",
                        data=final_content,
                        file_name=f"{local_master['title'].replace(' ', '_')}.txt",
                        mime="application/txt",
                        type="primary",
                    )
                with col4:
                    if st.button("Download as Doc", type="primary"):
                        st.warning('soon', icon="⚠️")
                with col5:
                    if st.button("Download as PDF", type="primary"):
                        st.warning('soon', icon="⚠️")
