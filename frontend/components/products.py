import streamlit as st
import pandas as pd
from components.dfTable import build_table_html

from utils.icons import eye
from utils.utils import date_col


def show_product(value: object) -> object:
    return f"<a href='/masterProductPage?id={value}' target='_self'>️{eye()}</a>"


def build_products_df(dataframe):
    # reorder
    new_column_order = ['title', 'url', 'created_at', 'id']
    dataframe = dataframe[new_column_order]
    # change names
    new_column_order = {'title': 'Title', 'url': 'Url', 'created_at': 'Creation Date', 'id': 'Actions'}
    dataframe = dataframe.rename(columns=new_column_order)
    # styling
    dataframe['Creation Date'] = dataframe['Creation Date'].apply(date_col)
    dataframe['Actions'] = dataframe['Actions'].apply(show_product)

    return dataframe


def display_products(all_products, with_filter):
    df = pd.DataFrame(all_products)
    df = build_products_df(df)
    build_table_html(df, with_filter, ['Title', 'Creation Date'])
