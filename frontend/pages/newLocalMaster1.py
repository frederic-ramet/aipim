import streamlit as st
from components import sidebar
from middleware.local_master_service import generate_local_product
from middleware.market_service import fetch_all_markets, generate_prompt
from middleware.product_service import fetch_master_product_by_id
from middleware.settings_service import get_full_settings
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
    full_settings = get_full_settings()
    all_features = full_settings.get('features').keys()
    all_marketAxis = full_settings.get('marketAxis').keys()
    main_card = generate_main_card('NEW LOCAL MASTER for: ' + master_product['title'])
    markets = fetch_all_markets()
    # Extract titles from the list of market dictionaries
    market_titles = [market['label'] for market in markets]
    with main_card:
        if master_product:
            left, right = st.columns([1, 4])
            with left:
                centered_text('Please provide the next informations', 'gray', 'left', 18, '')
                st.write('')
                centered_text('Select the market', 'black', 'left', 18, 'bold')

            with right:
                st.write('')
                selected_market_title = st.selectbox('', market_titles)
            selected_market = select_market_by_title(markets, selected_market_title)
            selected_market_id = selected_market["id"]
        centered_text('To be applied Prompt (you can edit them):', 'black', 'left', 18)
        custom_css = "background-color: #FFF5F5;"
        second_card = container_with_border(custom_css)
        with second_card:
            marketing_features = parse_string_list(selected_market['features'])
            default_axis = parse_string_list(selected_market['marketingAxis'])
            languages = parse_string_list(selected_market['languages'])
            culturalTrends = parse_string_list(selected_market['trends'])
            seoKeywords = parse_string_list(selected_market['seoKeywords'])

            # Display the title and input field side by side
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write("Marketing features:")
            with col2:
                marketing_features_input = st.multiselect(
                    "Please select the marketing features",
                    all_features,
                    marketing_features)
                marketing_features_input = list_to_string_items(marketing_features_input)
            # Display the title and input field side by side
            col3, col4 = st.columns([1, 4])
            with col3:
                st.write("Marketing axis:")
            with col4:
                default_axis_input = st.multiselect(
                    "Please select the marketing axis",
                    all_marketAxis,
                    default_axis)
                default_axis_input = list_to_string_items(default_axis_input)

            # Display the title and input field side by side
            col5, col6 = st.columns([1, 4])
            with col5:
                st.write("Languages:")
            with col6:
                language_input = st.selectbox('Select output language', languages)

            # Display the title and input field side by side
            col7, col8 = st.columns([1, 4])
            with col7:
                st.write("Cultural Trends:")
            with col8:
                culturalTrends_input = st.text_input("A list of Cultural Trends separated by comma", list_to_string_items(culturalTrends), key="cultural_trends_input")

            # Display the title and input field side by side
            col9, col10 = st.columns([1, 4])
            with col9:
                st.write("Seo Keywords:")
            with col10:
                seoKeywords_input = st.text_input(f"A list of Seo Keywords separated by comma. Keywords must be in {language_input}", list_to_string_items(seoKeywords), key="seo_keywords_input")

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
                    st.session_state['local_generated_content_market'] = selected_market_title
                    st.session_state['local_generated_content_lang'] = language_input
                    st.session_state.button_disabled = False  # Re-enable the button
                    st.switch_page('pages/newLocalMasterStep2.py')

            # Disable the button immediately on click
            def on_button_click():
                st.session_state.button_disabled = True
            # Button to generate content
            if st.button("Generate new content", type="primary", disabled=st.session_state.button_disabled,
                         on_click=on_button_click):
                generate_content()
            st.write('')
            st.write('')
