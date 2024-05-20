import streamlit as st
from components import sidebar
from middleware.market_service import fetch_all_markets, generate_prompt
from middleware.product_service import fetch_master_product_by_id, fetch_product
from utils.style import generate_main_container, generate_top_container, generate_main_card, centered_text, \
    container_with_border

params = st.query_params.to_dict()
product_id = params['id']
st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()
final_content=""
with home_container:
    master_product = fetch_master_product_by_id(product_id)
    main_card = generate_main_card('NEW LOCAL MASTER for: ' + master_product['title'])
    markets = fetch_all_markets()
    # Extract titles from the list of market dictionaries
    market_titles = [market['title'] for market in markets]

    with main_card:
        if 'step2' not in st.session_state:
            if master_product:
                left, right = st.columns([1, 4])
                with left:
                    centered_text('Step 1 (Generation):', 'black', 'left', 18, 'bold')
                    st.write('')
                    centered_text('Select the market', 'black', 'left', 18, 'bold')

                with right:
                    centered_text('Please provide the next informations', 'black', 'left', 18)
                    selected_market_title = st.selectbox('', market_titles)
                # Find the selected market dictionary based on the selected title
                selected_market = next((market for market in markets if market['title'] == selected_market_title), None)
                selected_market_id = selected_market["id"]
            centered_text('To be applied Prompt (you can edit them):', 'black', 'left', 18)
            custom_css = "background-color: #FFF5F5;"
            second_card = container_with_border(custom_css)
            with second_card:
                marketing_features = selected_market['marketFeatures']
                default_axis = selected_market['defaultAxis']
                languages = selected_market['languages']
                culturalTrends = selected_market['culturalTrends']
                seoKeywords = selected_market['seoKeywords']

                # Display the title and input field side by side
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.write("Marketing features:")
                with col2:
                    marketing_features_input = st.text_input("", marketing_features,
                                                             key="default_axis_features")  # st.selectbox('Marketing features', marketing_features)

                # Display the title and input field side by side
                col3, col4 = st.columns([1, 4])
                with col3:
                    st.write("Marketing axis:")
                with col4:
                    default_axis_input = st.text_input("", default_axis, key="default_axis_input")

                # Display the title and input field side by side
                col5, col6 = st.columns([1, 4])
                with col5:
                    st.write("Languages:")
                with col6:
                    languages_input = st.text_input("", languages, key="languages_input")

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
                new_market_settings = f"""
                    "marketFeatures":{marketing_features_input},
                    "defaultAxis":{default_axis_input},
                    "culturalTrends": {culturalTrends_input if culturalTrends_input else '""'},
                    "seoKeywords": {seoKeywords_input if seoKeywords_input else '""'},
                    "languages":{languages_input}
                """
                final_prompt = st.text_area("Prompt",
                                            generate_prompt(product_id, selected_market_id, new_market_settings),
                                            height=400)
            col1, col2, col3 = st.columns([4, 2, 4])
            with col2:
                if st.button("Generate new content", type="primary"):
                    final_content = "fdsfdsf"
                    st.session_state['step2'] = 'yes'
        else:
            test = st.text_area("Content", final_content, height=400)
            if st.button("Back", type="primary"):
                del st.session_state['step2']

        st.write(st.session_state['step2'])