import sqlite3
import json
from core.apps.content_creation import utils as cc_utils

    

def get_list_from_database(query):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute(query)

    # Fetch the first matching row
    row = db.fetchall()

    # Check if any rows were fetched
    if row:
        print(row)
    else:
        print("No data found in :", "market")

    # Close the connection
    conn.close()
        
    return row


def get_specific_info_from_database(query, parameter):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute(query,parameter)

    # Fetch the first matching row
    row = db.fetchall()

    # Check if any rows were fetched
    if row:
        print(row)
    else:
        print("No data found with id:", id)

    # Close the connection
    conn.close()
        
    return row[0]

def insert_generated_prompt_database(prompt, distributor_info, localMaster_info):

    distributorVersion_title =  f"{distributor_info['label']}_{distributor_info['format']}"
    distributorVersion_distributor = f"{distributor_info['label']}"
    distributorVersion_distributorId = f"{distributor_info['id']}"
    distributorVersion_settings = f""
    distributorVersion_prompt = prompt
    distributorVersion_content = ""
    distributorVersion_localMasterId = f"{localMaster_info['id']}"

    conn = sqlite3.connect('ai-pim.db')
    cursor = conn.cursor()
    
    # SQL command for inserting a new record
    sql = '''
        INSERT INTO distributorVersion ( title, distributor, distributorId, settings, prompt, content, localMasterId, created_at)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, datetime('now'))
    '''
    
    # Execute the SQL command
    cursor.execute(sql, (
        distributorVersion_title,
        distributorVersion_distributor,
        distributorVersion_distributorId,
        distributorVersion_settings,
        distributorVersion_prompt,
        distributorVersion_content,
        distributorVersion_localMasterId,
    ))
    
    # Commit the changes
    conn.commit()
    
    # Close the connection
    conn.close()


def distributor_prompt_generator(distributor_info, localMaster_info):
    generated_content = localMaster_info["content"]

    
    prompt = f""" product_details: {generated_content}

                distributor_title: {distributor_info["title"]}
                distributor_label: {distributor_info["label"]}
                distributor_description: {distributor_info["description"]}
                distributor_tone: {distributor_info["tone"]}
                distributor_defaultSettings: {distributor_info["defaultSettings"]}
                distributor_Format: {distributor_info["Format"]}
                distributor_seoKeywords: {distributor_info["seoKeywords"]}
                
                given info is regarding content generation for specific distributors.
                """
    insert_generated_prompt_database(prompt, distributor_info, localMaster_info )
    return prompt
    

def get_prompt_from_database(distributorVersion_id):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute("SELECT prompt FROM distributorVersion WHERE id = ?", (distributorVersion_id,))

    # Fetch the first matching row
    row = db.fetchone()

    # Check if any rows were fetched
    if row:
        print(row)
    else:
        print("No data found with distributorVersion_id:", distributorVersion_id)

    # Close the connection
    conn.close()
      
    return row


def insert_generated_content_database(generated_content, distributorVersion_id):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # Define the ID of the row you want to update
    row_id = distributorVersion_id 

    # Define the new value you want to set
    new_content = generated_content

    # Execute the UPDATE query
    db.execute('''
        UPDATE distributorVersion
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