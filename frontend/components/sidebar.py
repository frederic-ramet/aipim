import streamlit as st
from utils.style import set_style, generate_avatar, centered_text

def show_sidebar():
    # these are common sidebar for client and admin both
    st.sidebar.image("static/nexans_logo.png", width=200)  # Set image width
    st.sidebar.divider()
    st.sidebar.page_link("streamlit_app.py", label="Home")
    st.sidebar.page_link("pages/settings.py", label="Settings")

    set_style()
