import streamlit as st
import pandas as pd
from components.dfTable import build_table_html

from utils.icons import eye


def show_local_master(value: object) -> object:
    return f"<a href='/localMasterPage?id={value}' target='_self'>️{eye()}</a>"


def build_local_master_df(dataframe):
    # reorder
    new_column_order = ['title', 'marketName', 'settings', 'id']
    dataframe = dataframe[new_column_order]
    # change names
    new_column_order = {'title': 'Title', 'marketName': 'Market Name', 'settings': 'Settings', 'id': 'Actions'}
    dataframe = dataframe.rename(columns=new_column_order)
    dataframe['Actions'] = dataframe['Actions'].apply(show_local_master)

    return dataframe


def display_local_master_list(local_master_data, with_filter):
    df = pd.DataFrame(local_master_data)
    df = build_local_master_df(df)
    build_table_html(df, with_filter)
