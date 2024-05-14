import sqlite3
import requests
from bs4 import BeautifulSoup
import json

def get_market_info(selected_market:str):
    
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute("SELECT * FROM market WHERE title = ?", (selected_market,))

    # Fetch the first matching row
    row = db.fetchone()

    # Check if any rows were fetched
    if row:
        print(row)
    else:
        print("No data found with title:", selected_market)

    # Close the connection
    conn.close()
        
    return row
    


def generate_prompt_based_on_market_data(scraped_data_dict:dict, market_data:dict):
    prompt = f""" project details: {scraped_data_dict}

                Market_id: {market_data["id"]},"
                Market_title: {market_data["title"]},
                Market_languages: {market_data["languages"]},
                Market_defaultAxis: {market_data["defaultAxis"]},
                Market_defaultSettings: {market_data["defaultSettings"]},
                Market_marketFeatures: {market_data["marketFeatures"]},
                Market_culturalTrends: {market_data["culturalTrends"]},
                Market_seoKeywords: {market_data["seoKeywords"]},"
                
                
                CREATED PROMPTS.
                """
    return prompt
