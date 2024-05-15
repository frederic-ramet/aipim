import base64
import hashlib
import urllib
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stateful_button import button
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.switch_page_button import switch_page

hasher = hashlib.sha256()


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


def set_style():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def generate_avatar(email_value, size):
    default = "wavatar"
    email = email_value.strip().lower()
    email_bytes = email.encode('utf-8')
    hashed = hashlib.md5(email_bytes)
    hashed_email = hashed.hexdigest()

    # construct the url
    gravatar_url = f"https://gravatar.com/avatar/{hashed_email}?"
    gravatar_url += urllib.parse.urlencode({'d': default, 's': str(size), 'f': 'y'})
    return gravatar_url


def generate_top_container(title):
    top_container = stylable_container(key="top_container",
                                       css_styles="""
                                    {
                                        padding: 10px;
                                        background: white;
                                        overflow: hidden;
                                        margin-top: 10px;
                                        width: 100%;
                                    }
                                """)
    with top_container:
        colored_header(
            label=title,
            description="",
            color_name="red-70",
        )

    return top_container


def generate_main_container():
    return stylable_container(key="main_container",
                              css_styles="""
                                    {
                                        background: #F5F6FA;
                                        padding: 10px;
                                        overflow: hidden;
                                        border-radius: 5px;
                                        height: 100%;
                                    }
                                """)


def centered_text(text, color='black', direction='left', size=20, bold='bold'):
    return st.markdown(
        f"<div style='text-align: {direction}; color: {color}; font-size:{size}px; font-weight: {bold};'>{text}</div>",
        unsafe_allow_html=True)


def hr():
    return st.markdown("<hr style='padding: 0px;margin: 0 5px;width: 95%;'/>", unsafe_allow_html=True)


def generate_main_card(title='', right_actions=None):
    if right_actions is None:
        right_actions = []

    main_card_container = stylable_container(key="main_card",
                                             css_styles="""
                                        {
                                            background: white;
                                            padding: 20px;                                                                              
                                            overflow: hidden;
                                            margin-top: 5px;
                                            border-radius: 15px;
                                        }
                                    """)

    with main_card_container:
        title_col, actions_col = st.columns([3, 2])
        with title_col:
            centered_text(title, '#8D8D8D', 'left', 18, 'bold')
        with actions_col:
            if len(right_actions) > 0:
                colns = st.columns(len(right_actions))
                for i, col in enumerate(colns):
                    with col:
                        action = right_actions[i]
                        if button(action['text'], key=action['key'], type=action['type']):
                            if action['key'] in st.session_state:
                                st.session_state[action['key']] = None
                            switch_page(action['page'])
        hr()

    return main_card_container
