import pandas as pd
from components.dfTable import build_table_html
from utils.utils import date_col


def show_product(value: object) -> object:
    return f"<a href='/masterProductPage?id={value}' target='_self'><i class='fa fa-regular fa-eye' style='color: " \
           f"#31333f;'></i></a>"


def delete_product(value: object) -> object:
    return f" <a href='/?delete_master_product={value}' target='_self'><i class='fa fa-solid fa-trash' " \
           f"style='color: #EE2426;'></i></a>"


def make_clickable(url: str) -> str:
    return f'<a href="{url}" target="_blank">{url}</a>'


def build_products_df(dataframe):
    dataframe['delete'] = dataframe['id']
    # reorder
    new_column_order = ['title', 'url', 'created_at', 'id', 'delete']
    dataframe = dataframe[new_column_order]
    # change names
    new_column_names = {'title': 'Title', 'url': 'Url', 'created_at': 'Creation Date', 'id': 'Show', 'delete': 'Delete'}
    dataframe = dataframe.rename(columns=new_column_names)
    # make urls clickable
    dataframe['Url'] = dataframe['Url'].apply(make_clickable)
    # styling
    dataframe['Creation Date'] = dataframe['Creation Date'].apply(date_col)
    dataframe['Show'] = dataframe['Show'].apply(show_product)
    dataframe['Delete'] = dataframe['Delete'].apply(delete_product)

    return dataframe


def display_products(all_products, with_filter):
    df = pd.DataFrame(all_products)
    df = build_products_df(df)
    build_table_html(df, with_filter, ['Title', 'Creation Date'])
