import streamlit as st
from components import sidebar
from components.products import display_local_master_list
from middleware.market_service import fetch_all_markets, generate_prompt_test
from middleware.product_service import fetch_master_product_by_id, fetch_product
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, hr, \
    generate_card, container_with_border

params = st.query_params.to_dict()
product_id = 1  #;params['id']
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
                centered_text('Please provide the next informations:', 'black', 'left', 18)
                selected_market_title = st.selectbox('', market_titles)
            # Find the selected market dictionary based on the selected title
            selected_market = next((market for market in markets if market['title'] == selected_market_title), None)
            selected_market_id = selected_market["id"]
        centered_text('To be applied Prompt (you can edit them):', 'black', 'left', 18)
        custom_css = "background-color: #FFF5F5;"
        second_card = container_with_border(custom_css)
        with second_card:
            default_axis = selected_market['defaultAxis']
            marketing_features = selected_market['marketFeatures']
            languages = selected_market['languages']
            culturalTrends = selected_market['culturalTrends']
            seoKeywords = selected_market['seoKeywords']

            # Display the title and input field side by side
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write("Marketing features:")
            with col2:
                marketing_features_input = st.text_input("Marketing features", marketing_features,
                                                         key="marketing_features_input")

            # Display the title and input field side by side
            col3, col4 = st.columns([1, 4])
            with col3:
                st.write("Marketing axis:")
            with col4:
                default_axis_input = st.text_input("Marketing axis", default_axis, key="default_axis_input")

            # Display the title and input field side by side
            col5, col6 = st.columns([1, 4])
            with col5:
                st.write("Languages:")
            with col6:
                languages_input = st.text_input("Languages", languages, key="languages_input")

            # Display the title and input field side by side
            col7, col8 = st.columns([1, 4])
            with col7:
                st.write("Cultural Trends:")
            with col8:
                culturalTrends_input = st.text_input("Cultural Trends", culturalTrends, key="cultural_trends_input")

            # Display the title and input field side by side
            col9, col10 = st.columns([1, 4])
            with col9:
                st.write("Seo Keywords:")
            with col10:
                seoKeywords_input = st.text_input("Seo Keywords", seoKeywords, key="seo_keywords_input")

        centered_text('To be applied Prompt (you can edit them):', 'black', 'left', 18)
        prompt_card = container_with_border(custom_css)
        with prompt_card:
            st.write('Here’s go the content of the generated prompt ...')
            data = {
                "master_product_id": product_id,
                "selected_market_id": selected_market_id,
                "market_settings": "['Mobiway', 'Twistal']"
            }
            #generate_prompt(data)
            generate_prompt_test(1,1,"['Mobiway', 'Twistal']")
        col1, col2, col3 = st.columns([4, 2, 4])
        with col2:
            if st.button("Generate new content", type="primary"):
                st.switch_page("pages/localMasterStep2.py")
