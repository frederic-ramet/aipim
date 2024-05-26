import streamlit as st
from components import sidebar
from components.distributors import display_distributors_versions_list
from middleware.local_master_service import fetch_local_master_by_id
from middleware.distributor_service import fetch_all_distributors_versions
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, createBtn, container_with_colored_bg
from utils.utils import parse_market_settings

st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")

params = st.query_params.to_dict()
local_master_id = params['id']
product_id = params['product_id']

sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM ")
home_container = generate_main_container()

with home_container:
    local_master = fetch_local_master_by_id(local_master_id)
    main_card = generate_main_card('LOCAL MASTER for: ' + local_master['title'])
    with main_card:
        if local_master:
            centered_text(f"Selected market <i>{local_master.get('marketName')}</i>", 'black', 'left', 18, 'bold')
            centered_text('Applied settings', 'black', 'left', 18, 'bold')
            with st.expander("Show"):
                settings = local_master.get('settings')
                if settings:
                    settings_obj = parse_market_settings(settings)
                    st.write(settings_obj)
                else:
                    st.warning("No settings available for this local master.")

            centered_text('Used Prompt', 'black', 'left', 18, 'bold')
            with st.expander("Show"):
                st.write(local_master.get('prompt'))

            centered_text('Generated content', 'black', 'left', 18, 'bold')
            with st.expander("Show"):
                st.markdown(f"<pre>{local_master.get('content')}</pre>", unsafe_allow_html=True)
            centered_text('Distributor versions', 'black', 'left', 18, 'bold')
            distributors_versions = fetch_all_distributors_versions(local_master_id)
            if distributors_versions:
                display_distributors_versions_list(product_id, distributors_versions, True)
                st.write('')
        else:
            st.error("Local master not found.")
        col1, col2, col3, col4 = st.columns([2, 4, 4, 2])
        with col2:
            createBtn(f'/masterProductPage?id={product_id}', 'Back')
        with col3:
            createBtn(f'/newDistributorVersion?local_master_id={local_master_id}&product_id={product_id}', 'Generate New DISTRIBUTOR VERSION')


