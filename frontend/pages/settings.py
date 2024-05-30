import streamlit as st
import json
from components import sidebar
from middleware.settings_service import update_markets, get_full_settings
from utils.style import generate_main_container, generate_top_container, generate_main_card


st.set_page_config(page_title="Ai-Pim Backoffice", layout="wide")
sidebar.show_sidebar()
generate_top_container("Welcome to AI PIM")
home_container = generate_main_container()

json_data = ""

with home_container:
    main_card = generate_main_card("Platform Settings")

    full_settings = get_full_settings()
    markets = full_settings.get('market')
    distributors = full_settings.get('distribution')
    all_features = full_settings.get('features')
    print(all_features)
    all_marketAxis = full_settings.get('marketAxis')

    with main_card:
        markets_tab, distributors_tab, features_tab, axis_tab = st.tabs(
            ["Markets", "Distributors", "Features", "Marketing Axis"])

        with markets_tab:
            left_col, right_col = st.columns(2)
            with left_col:
                markets_str = json.dumps(markets, indent=4)
                edited_markets_str = st.text_area("Please edit markets' settings here", value=markets_str, height=400)
                if st.button("Save markets", type="primary"):
                    updated = update_markets(edited_markets_str)
                    if updated is not None:
                        st.success("Markets' setting have been saved", icon="✅")

            with right_col:
                try:
                    edited_markets = json.loads(edited_markets_str)
                    st.write(edited_markets)
                except json.JSONDecodeError:
                    st.error("Not a valid JSON.")

        with distributors_tab:
            left_col, right_col = st.columns(2)
            with left_col:
                distributors_str = json.dumps(distributors, indent=4)
                edited_distributors_str = st.text_area("Please edit distributors' settings here", value=distributors_str,
                                                       height=400)
                if st.button("Save distributors", type="primary"):
                    st.success("Distributors' setting have been saved", icon="✅")
            with right_col:
                try:
                    edited_distributors = json.loads(edited_distributors_str)
                    st.write(edited_distributors)
                except json.JSONDecodeError:
                    st.error("Not a valid JSON.")

        with features_tab:
            left_col, right_col = st.columns(2)
            with left_col:
                features_str = json.dumps(all_features, indent=4)
                edited_features_str = st.text_area("Please edit features' settings here", value=features_str, height=400)
                if st.button("Save features", type="primary"):
                    st.write('saved')
            with right_col:
                try:
                    edited_features = json.loads(edited_features_str)
                    st.write(edited_features)
                except json.JSONDecodeError:
                    st.error("Not a valid JSON.")

        with axis_tab:
            left_col, right_col = st.columns(2)
            with left_col:
                axis_str = json.dumps(all_marketAxis, indent=4)
                edited_axis_str = st.text_area("Please edit market axis' settings here", value=axis_str, height=400)
                if st.button("Save axis", type="primary"):
                    st.write('saved')
            with right_col:
                try:
                    edited_axis = json.loads(edited_axis_str)
                    st.write(edited_axis)
                except json.JSONDecodeError:
                    st.error("Not a valid JSON.")