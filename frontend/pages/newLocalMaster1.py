import streamlit as st
from components import sidebar
from middleware.local_master_service import generate_local_product
from middleware.market_service import fetch_all_markets, generate_prompt
from middleware.product_service import fetch_master_product_by_id
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, \
    container_with_border
from utils.utils import select_market_by_title, parse_string_list, list_to_string_items, string_items_to_string_list

params = st.query_params.to_dict()
product_id = params['id']
st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

with home_container:
    master_product = fetch_master_product_by_id(product_id)
    main_card = generate_main_card('NEW LOCAL MASTER for: ' + master_product['title'])
    markets = fetch_all_markets()
    # Extract titles from the list of market dictionaries
    market_titles = [market['title'] for market in markets]
    with main_card:
        if master_product:
            left, right = st.columns([1, 4])
            with left:
                centered_text('Step 1 (Generation):', 'black', 'left', 18, 'bold')
                st.write('')
                centered_text('Select the market', 'black', 'left', 18, 'bold')

            with right:
                centered_text('Please provide the next informations', 'black', 'left', 18)
                selected_market_title = st.selectbox('', market_titles)
            selected_market = select_market_by_title(markets, selected_market_title)
            selected_market_id = selected_market["id"]
        centered_text('To be applied Prompt (you can edit them):', 'black', 'left', 18)
        custom_css = "background-color: #FFF5F5;"
        second_card = container_with_border(custom_css)
        with second_card:
            marketing_features = parse_string_list(selected_market['marketFeatures'])
            default_axis = parse_string_list(selected_market['defaultAxis'])
            languages = parse_string_list(selected_market['languages'])
            culturalTrends = parse_string_list(selected_market['culturalTrends'])
            seoKeywords = parse_string_list(selected_market['seoKeywords'])

            # Display the title and input field side by side
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write("Marketing features:")
            with col2:
                marketing_features_input = st.text_input("a list of marketing features separated by ',' ", list_to_string_items(marketing_features),
                                                         key="default_marketing_features")

            # Display the title and input field side by side
            col3, col4 = st.columns([1, 4])
            with col3:
                st.write("Marketing axis:")
            with col4:
                default_axis_input = st.text_input("a list of marketing axis separated by ',' ",  list_to_string_items(default_axis), key="default_axis_input")

            # Display the title and input field side by side
            col5, col6 = st.columns([1, 4])
            with col5:
                st.write("Languages:")
            with col6:
                language_input = st.selectbox('select output language', languages)

            # Display the title and input field side by side
            col7, col8 = st.columns([1, 4])
            with col7:
                st.write("Cultural Trends:")
            with col8:
                culturalTrends_input = st.text_input("a list of Cultural Trends separated by',' ", list_to_string_items(culturalTrends), key="cultural_trends_input")

            # Display the title and input field side by side
            col9, col10 = st.columns([1, 4])
            with col9:
                st.write("Seo Keywords:")
            with col10:
                seoKeywords_input = st.text_input("a list of Seo Keywords separated by',' ", list_to_string_items(seoKeywords), key="seo_keywords_input")

        centered_text('To be applied Prompt (you can edit them):', 'black', 'left', 18)
        prompt_card = container_with_border(custom_css)
        with prompt_card:
            st.write('Here’s go the content of the generated prompt ...')
            new_market_settings = f"""
                    "marketFeatures":{string_items_to_string_list(marketing_features_input)},
                    "defaultAxis":{string_items_to_string_list(default_axis_input)},
                    "culturalTrends": {string_items_to_string_list(culturalTrends_input)},
                    "seoKeywords": {string_items_to_string_list(seoKeywords_input)},
                    "languages": '{language_input}'
                """
            new_market_settings = "{"+new_market_settings+"}"
            final_prompt = st.text_area("Prompt",
                                        generate_prompt(product_id, selected_market_id, new_market_settings),
                                        height=400)

        col1, col2, col3 = st.columns([4, 2, 4])

        with col2:
            # Initialize session state for the button if not already done
            if 'button_disabled' not in st.session_state:
                st.session_state.button_disabled = False

            def generate_content():
                with st.spinner('Generating content...'):
                    final_content = generate_local_product(product_id, selected_market_id, new_market_settings,
                                                           final_prompt)
                    st.session_state['local_generated_product_id'] = product_id
                    st.session_state['local_generated_content'] = final_content
                    st.session_state.button_disabled = False  # Re-enable the button
                    st.switch_page('pages/newLocalMasterStep2.py')

            # Disable the button immediately on click
            def on_button_click():
                st.session_state.button_disabled = True
                #st.experimental_rerun() ?? important or not ??
            # Button to generate content
            if st.button("Generate new content", type="primary", disabled=st.session_state.button_disabled,
                         on_click=on_button_click):
                generate_content()
