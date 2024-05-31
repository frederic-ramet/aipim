import pandas as pd
import requests
import streamlit as st
from bs4 import BeautifulSoup


def search_over_nexans(keyword):
    url = f"https://www.nexans.fr/fr/search.html?view=all&page=1&query={keyword}"  # Replace with the target URL
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the target element
        search_results = soup.find('ul', class_='search__results')

        # Extract element text or attributes as needed
        element_list = []
        if search_results:
            for li in search_results.find_all('li'):
                link = li.find('a')['href']
                if '/products' in link:
                    element_list.append({
                        'title': li.find('a').text.strip(),
                        'link': 'https://www.nexans.fr' + li.find('a')['href']
                    })
        print(element_list)
        return element_list
    else:
        print("Error fetching webpage content!")
        return []


def fetch_link(value: object) -> object:
    return f"<a href='/addProduct?url={value}' target='_self'>Import product reference</a>"


def show_link(value: object) -> object:
    return f"<a href='{value}'>show</a>"


def display_search_results(results):
    if len(results) > 0:
        table_container = st.container()
        with table_container:
            df = pd.DataFrame(results)
            df['Fetch'] = df['link'].apply(fetch_link)
            df['link'] = df['link'].apply(show_link)
            html_text = df.to_html(escape=False)
            st.markdown(html_text, unsafe_allow_html=True)
