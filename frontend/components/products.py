import streamlit as st
import pandas as pd
from components.dfTable import build_table_html

from utils.icons import eye


def show_product(value: object) -> object:
    return f"<a href='/masterProductPage?id={value}' target='_self'>️{eye()}</a>"


def build_products_df(dataframe):
    # reorder
    new_column_order = ['title', 'url', 'description', 'created_at', 'id']
    dataframe = dataframe[new_column_order]
    # change names
    new_column_order = {'title': 'Title', 'url': 'Url', 'id': 'Actions'}
    dataframe = dataframe.rename(columns=new_column_order)
    # styling
    # dataframe['Creation Date'] = dataframe['Creation Date'].apply(date_col)
    dataframe['Actions'] = dataframe['Actions'].apply(show_product)
    # dataframe['Avatar'] = dataframe['Avatar'].apply(show_avatar)

    return dataframe


def display_products(all_products, with_filter):
    df = pd.DataFrame(all_products)
    df = build_products_df(df)
    build_table_html(df, with_filter)


