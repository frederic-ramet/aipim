import streamlit as st
from components import sidebar
from middleware.local_master_service import fetch_local_master_by_id
from middleware.distributor_service import fetch_all_distributors, generate_prompt_distributor, \
    generate_distributor_version
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, \
    container_with_border, createBtn
from utils.utils import select_distributor_by_label, string_items_to_string_list, string_items_to_list, \
    build_list_as_string

params = st.query_params.to_dict()
local_master_id = params['local_master_id']
product_id = params['product_id']
st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

with home_container:
    local_master = fetch_local_master_by_id(local_master_id)
    language = eval(local_master['settings'])['languages']
    main_card = generate_main_card(
        f"New DISTRIBUTOR VERSION for Product reference: {local_master['title']} | {local_master['marketName']}")
    distributors = fetch_all_distributors()
    # Extract labels from the list of distributors dictionaries
    distributors_labels = [distributor['label'] for distributor in distributors]
    with main_card:
        if local_master:
            left, right = st.columns([1, 4])
            with left:
                centered_text('Please provide the next informations', 'gray', 'left', 18, '')
                st.write('')
                centered_text('Select the distributor', 'black', 'left', 18, 'bold')

            with right:
                centered_text('Please provide the next information', 'black', 'left', 18)
                selected_distributor_label = st.selectbox('', distributors_labels)

            selected_distributor = select_distributor_by_label(distributors, selected_distributor_label)
            print(selected_distributor)
            selected_distributor_id = selected_distributor['id']
        centered_text('To be applied settings (you can edit them):', 'black', 'left', 18)
        custom_css = "background-color: #FFF5F5;"
        second_card = container_with_border(custom_css)
        with second_card:
            titleRecommendations = selected_distributor['titleRecommendations']
            descRecommendations = selected_distributor['descRecommendations']
            tone = selected_distributor['tone']
            target = str(selected_distributor['target'])
            distributor_settings = ""  # selected_distributor['defaultSettings']
            seoKeywords = str(selected_distributor['seoKeywords'])

            # Display the title and input field side by side
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write("Title:")
            with col2:
                distributor_title_input = st.text_input("Title recommendations", titleRecommendations)

            # Display the title and input field side by side
            col3, col4 = st.columns([1, 4])
            with col3:
                st.write("Description:")
            with col4:
                distributor_description_input = st.text_input("Description recommendations", descRecommendations)
            # Display the title and input field side by side
            col5, col6 = st.columns([1, 4])
            with col5:
                st.write("Main target:")
            with col6:
                targets = string_items_to_list(target)
                distributor_format_input = st.multiselect(
                    "Please select the targeting marketing type",
                    targets,  # backend get all targets
                    targets)
                # distributor_format_input = list_to_string_items(marketing_features_input)
                # distributor_ton_input = st.text_input("Target Market", target)

            # Display the title and input field side by side
            col7, col8 = st.columns([1, 4])
            with col7:
                st.write("Tone:")
            with col8:
                distributor_ton_input = st.text_area("Tone", tone, height=100)
            # Display the title and input field side by side

        centered_text('To be applied Prompt (you can edit them):', 'black', 'left', 18)
        prompt_card = container_with_border(custom_css)
        with prompt_card:
            st.write('Here’s go the content of the generated prompt ...')
            new_distributor_settings = f"""
                                "label":"{selected_distributor_label}",
                                "description": "",
                                "titleRecommendations":"{distributor_title_input}",
                                "descRecommendations":"{descRecommendations}",
                                "tone": "{distributor_ton_input}",
                                "target": {build_list_as_string(distributor_format_input)},
                                "language": "{language}",
                                "seoKeywords": {seoKeywords},
                            """
            new_distributor_settings = "{" + new_distributor_settings + "}"
            final_prompt = st.text_area("Prompt", generate_prompt_distributor(selected_distributor_id, local_master_id,
                                                                              new_distributor_settings), height=400)
        #
        col1_1, col2_1, col3_1, col4_1 = st.columns([2, 4, 4, 2])
        with col2_1:
            createBtn(f'/localMasterPage?id={local_master_id}&product_id={product_id}', 'Back')
        with col3_1:
            # Initialize session state for the button if not already done
            if 'button_disabled' not in st.session_state:
                st.session_state.button_disabled = False


            def generate_distributor_version_content():
                with st.spinner('Generating distributor version...'):
                    final_content = generate_distributor_version(selected_distributor_id, local_master_id,
                                                                 distributor_settings, final_prompt)
                    st.session_state['local_master_id'] = local_master_id
                    st.session_state['product_id'] = product_id
                    st.session_state['selected_distributor'] = selected_distributor_label
                    st.session_state['distributor_version_content'] = final_content
                    st.session_state.button_disabled = False  # Re-enable the button
                    st.switch_page('pages/newDistributorVersion2.py')


            # Disable the button immediately on click
            def on_button_click():
                st.session_state.button_disabled = True


            # Button to generate content
            if st.button("Generate a new distributor version", type="primary",
                         disabled=st.session_state.button_disabled,
                         on_click=on_button_click):
                generate_distributor_version_content()
