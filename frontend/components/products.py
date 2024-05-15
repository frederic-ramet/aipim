import streamlit as st
import pandas as pd
import components.dfTable
import components.utils


def build_products_df(dataframe):
    dataframe['avatar'] = dataframe['email']
    # reorder
    new_column_order = ['product', 'url', 'market', 'id']
    dataframe = dataframe[new_column_order]
    # change names
    new_column_order = {'product': 'Product', 'url': 'Url', 'id': 'Actions'}
    dataframe = dataframe.rename(columns=new_column_order)
    # styling
    dataframe['Creation Date'] = dataframe['Creation Date'].apply(date_col)
    dataframe['User Status'] = dataframe['User Status'].apply(map_status)
    # dataframe['Actions'] = dataframe['Actions'].apply(show_user)
    # dataframe['Avatar'] = dataframe['Avatar'].apply(show_avatar)

    return dataframe


def display_products(all_products, with_filter):
    df = pd.DataFrame(all_products)
    df = build_products_df(df)
    build_table_html(df, with_filter)


def display_product(product_data):
    df = pd.DataFrame([product_data])
    st.dataframe(df)
