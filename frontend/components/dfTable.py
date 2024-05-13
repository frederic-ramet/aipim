import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer


def build_table(dataframe, column_config, with_filter):
    table_container = st.container()
    with table_container:
        if with_filter:
            filtered_df = dataframe_explorer(dataframe, case=False)
            st.dataframe(filtered_df, column_config=column_config, use_container_width=True, hide_index=True)
        else:
            st.dataframe(dataframe, column_config=column_config, use_container_width=True, hide_index=True)

    return table_container


def build_table_html(dataframe, with_filter):
    table_container = st.container()
    with table_container:
        if with_filter:
            filtered_df = dataframe_explorer(dataframe, case=False)
            html_text = filtered_df.to_html(escape=False)
            html_text = html_text.replace('target="_blank"', "")
            st.markdown(html_text, unsafe_allow_html=True)
        else:
            html_text = dataframe.to_html(escape=False)
            html_text = html_text.replace('target="_blank"', "")
            st.markdown(html_text, unsafe_allow_html=True)

    return table_container
