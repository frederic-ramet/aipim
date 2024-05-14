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
    

def local_products_list(masterProductId:int):
    
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute("SELECT * FROM localMaster WHERE masterProductId = ?", (masterProductId,))

    # Fetch the first matching row
    row = db.fetchall()

    # Check if any rows were fetched
    if row:
        print(row)
    else:
        print("No data found with masterProductId:", masterProductId)

    # Close the connection
    conn.close()
        
    return row
    
def store_prompt_to_database(prompt, market_data, master_product_id):

    
    local_master_title = f"{market_data['title']}_{market_data['languages'][0]}"
    local_market_name = market_data["title"]
    local_market_id = market_data["id"]
    local_market_settings = ""
    local_market_prompt = prompt
    local_market_content = ""
    local_market_master_product_id = master_product_id
    
    conn = sqlite3.connect('ai-pim.db')
    cursor = conn.cursor()
    
    # SQL command for inserting a new record
    sql = '''
        INSERT INTO localMaster ( title ,marketName ,marketId ,settings ,prompt ,content ,masterProductId, created_at)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, datetime('now'))
    '''
    
    # Execute the SQL command
    cursor.execute(sql, (
        local_master_title,
        local_market_name,
        local_market_id,
        local_market_settings,
        local_market_prompt,
        local_market_content,
        local_market_master_product_id,
    ))
    
    # Commit the changes
    conn.commit()
    
    # Close the connection
    conn.close()
    

def get_scrapped_data_from_database(master_product_id):
    
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute("SELECT content FROM masterProduct WHERE id = ?", (master_product_id,))

    # Fetch the first matching row
    row = db.fetchone()

    # Check if any rows were fetched
    if row:
        print(row)
    else:
        print("No data found with masterProductId:", master_product_id)

    # Close the connection
    conn.close()
      
    return row
    
def generate_prompt_based_on_market_data(scraped_data_dict:str, market_data:dict,  master_product_id:int):
    
    
    prompt = f""" project details: {scraped_data_dict}

                Market_id: {market_data["id"]},"
                Market_title: {market_data["title"]},
                Market_languages: {market_data["languages"]},
                Market_defaultAxis: {market_data["defaultAxis"]},
                Market_defaultSettings: {market_data["defaultSettings"]},
                Market_marketFeatures: {market_data["marketFeatures"]},
                Market_culturalTrends: {market_data["culturalTrends"]},
                Market_seoKeywords: {market_data["seoKeywords"]},"
                
                CREATE PROMPTS.
                """
    store_prompt_to_database(prompt, market_data, master_product_id)
    return prompt

def insert_generated_content_database(generated_content, local_master_id):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # Define the ID of the row you want to update
    row_id = local_master_id 

    # Define the new value you want to set
    new_content = generated_content

    # Execute the UPDATE query
    db.execute('''
        UPDATE localMaster
        SET content = ?
        WHERE id = ?
    ''', (new_content, row_id))

    # Commit the changes
    conn.commit()

    # Check if any row was updated
    if db.rowcount > 0:
        print("Cell updated successfully.")
    else:
        print("No row found with ID:", row_id)

    # Close the connection
    conn.close()

def get_prompt_from_database(local_master_id):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute("SELECT prompt FROM localMaster WHERE id = ?", (local_master_id,))

    # Fetch the first matching row
    row = db.fetchone()

    # Check if any rows were fetched
    if row:
        print(row)
    else:
        print("No data found with local_master_id:", local_master_id)

    # Close the connection
    conn.close()
      
    return row