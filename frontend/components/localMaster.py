import streamlit as st
import pandas as pd
from components.dfTable import build_table_html

from utils.icons import eye
from utils.utils import date_col


def show_local_master(value: object) -> object:
    product_id = st.session_state['product_id']
    return f"<a href='/localMasterPage?id={value}&product_id={product_id}' target='_self'><i class='fa fa-regular " \
           f"fa-eye' style='color:#31333f;'></i></a>"


def delete_local_master(value: object) -> object:
    product_id = st.session_state['product_id']
    return f" <a href='/masterProductPage?id={product_id}&delete_local_product={value}' target='_self'><i class='fa " \
           f"fa-solid fa-trash' style='color: #EE2426;'></i></a>"


def build_local_master_df(dataframe):
    dataframe['delete'] = dataframe['id']
    # reorder
    new_column_order = ['title', 'marketName', 'created_at', 'id', 'delete']
    dataframe = dataframe[new_column_order]
    # change names
    new_column_order = {'title': 'Title', 'marketName': 'Market Name', 'created_at': 'Creation Date', 'id': 'Show',
                        'delete': 'Delete'}
    dataframe = dataframe.rename(columns=new_column_order)
    dataframe['Creation Date'] = dataframe['Creation Date'].apply(date_col)
    dataframe['Show'] = dataframe['Show'].apply(show_local_master)
    dataframe['Delete'] = dataframe['Delete'].apply(delete_local_master)
    return dataframe


def display_local_master_list(product_id, local_master_data, with_filter):
    st.session_state['product_id'] = product_id
    df = pd.DataFrame(local_master_data)
    df = build_local_master_df(df)
    build_table_html(df, with_filter, ['Title', 'Market Name', 'Creation Date'])
