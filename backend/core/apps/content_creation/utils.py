import sqlite3
import json


def get_market_info(selected_market_id: int):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute("SELECT * FROM market WHERE id = ?", (selected_market_id,))

    # Fetch the first matching row
    row = db.fetchone()

    # Check if any rows were fetched
    if row:
        print("Data fetch successfully.")
    else:
        print("No data found with id:", selected_market_id)

    # Close the connection
    conn.close()

    return row


def local_products_list(masterProductId: int):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute("SELECT * FROM localMaster WHERE masterProductId = ?", (masterProductId,))

    # Fetch the first matching row
    row = db.fetchall()

    # Check if any rows were fetched
    if row:
        print("Data fetch successfully.")
    else:
        print("No data found with masterProductId:", masterProductId)

    # Close the connection
    conn.close()

    return row


def store_info_in_to_database(prompt, market_data, master_product_id, selected_market_id, market_info_from_database,
                              content, scrapped_data_dict):
    local_master_title = f"{scrapped_data_dict['title']}"
    local_master_name =  f"{market_info_from_database['title']}"
    local_master_id = selected_market_id
    local_master_settings = market_data
    local_master_prompt = prompt
    local_master_content = content
    local_master_master_product_id = master_product_id

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
        local_master_name,
        local_master_id,
        local_master_settings,
        local_master_prompt,
        local_master_content,
        local_master_master_product_id,
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
        print("Data fetch successfully.")
    else:
        print("No data found with masterProductId:", master_product_id)

    # Close the connection
    conn.close()

    return row


def generate_prompt_based_on_market_data(scraped_data_dict: str, selected_market_id: int, market_data: str):
    market_data_dict = eval(market_data)
    market_info_from_database = get_market_info(selected_market_id)

    market_axis_list = market_data_dict["defaultAxis"]
    market_features_list = market_data_dict["marketFeatures"]
    seo_keywords = market_data_dict["seoKeywords"]
    trends = market_data_dict["culturalTrends"]

    with open('static/parameters/feature.json', 'r') as file_feature:
        features_data = json.load(file_feature)

    with open('static/parameters/marketing_axis.json', 'r') as file_axis:
        axis_data = json.load(file_axis)

    market_axis_dict = {}
    for axis in market_axis_list:
        market_axis_dict[axis] = axis_data[axis]

    market_features_dict = {}
    for feature in market_features_list:
        market_features_dict[feature] = features_data[feature]

    prompt = f""" 
                Generate a Local master product content for the market {market_info_from_database['title']}.
                Here are this product information:
                Main details: {scraped_data_dict}
                Market_data: {market_data},
                Market_axis: {market_axis_dict},
                Market_features: {market_features_dict},
                Seo keywords: {seo_keywords},
                trends: {trends},
                Content must be optimized to SEO.
                """

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
        print("Data fetch successfully.")
    else:
        print("No data found with local_master_id:", local_master_id)

    # Close the connection
    conn.close()

    return row


def get_one_local_master_from_database(id: int):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute("SELECT * FROM localMaster WHERE id = ?", (id,))

    # Fetch the first matching row
    row = db.fetchall()

    # Check if any rows were fetched
    if row:
        print("Data fetch successfully.")
    else:
        print("No data found with id:", id)

    # Close the connection
    conn.close()

    return row[0]
