import streamlit as st
import pandas as pd
from components.dfTable import build_table_html

from utils.icons import eye
from utils.utils import date_col


def show_distributor_version(value: object) -> object:
    # product_id = st.session_state['product_id']
    return f"<a href='/distributorVersion' target='_self'>️{eye()}</a>"


def build_distributors_df(dataframe):
    # reorder
    new_column_order = ['title', 'label', 'description', 'id']
    dataframe = dataframe[new_column_order]
    # change names
    new_column_order = {'title': 'Title', 'label': 'lLabel', 'description': 'Description', 'id': 'Id'}
    dataframe = dataframe.rename(columns=new_column_order)
    # dataframe['Actions'] = dataframe['Actions'].apply(show_local_master)
    # dataframe['Creation Date'] = dataframe['Creation Date'].apply(date_col)
    return dataframe


def build_distributors_versions_df(dataframe):

    # reorder
    new_column_order = ['title', 'distributor', 'created_at', 'id']
    dataframe = dataframe[new_column_order]
    # change names
    new_column_order = {'title': 'Title', 'distributor': 'Distributor', 'created_at': 'Creation Date', 'id': 'Actions'}
    dataframe = dataframe.rename(columns=new_column_order)
    dataframe['Actions'] = dataframe['Actions'].apply(show_distributor_version)
    dataframe['Creation Date'] = dataframe['Creation Date'].apply(date_col)
    return dataframe


def display_distributors_list(product_id, distributors, with_filter):
    # st.session_state['product_id'] = product_id
    df = pd.DataFrame(distributors)
    df = build_distributors_df(df)
    build_table_html(df, with_filter)


def display_distributors_versions_list(product_id, distributors, with_filter):
    # st.session_state['product_id'] = product_id
    df = pd.DataFrame(distributors)
    df = build_distributors_versions_df(df)
    build_table_html(df, with_filter, ['Title', 'Distributor', 'Creation Date'])
