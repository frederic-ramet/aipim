import sqlite3
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
        print("Data fetch successfully.")
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
        print("Data fetch successfully.")
    else:
        print("No data found with id:", id)

    # Close the connection
    conn.close()
        
    return row[0]



def insert_info_to_database(distributorVersion_title, distributorVersion_distributor, distributorVersion_distributorId, distributorVersion_settings, distributorVersion_prompt, distributorVersion_content, distributorVersion_localMasterId):

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


def distributor_prompt_generator(distributor_info_from_database:dict, localMaster_info_from_database:dict, distributor_settings:str):

    generated_content = localMaster_info_from_database["content"]
    prompt = f""" product_details: {generated_content}
                distributor_data: {distributor_settings},
                given info is regarding content generation for specific distributors.
                """
    #insert_generated_prompt_database(prompt, distributor_info_from_database, localMaster_info_from_database, distributor_settings)
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
        print("Data fetch successfully.")
    else:
        print("No data found with distributorVersion_id:", distributorVersion_id)

    # Close the connection
    conn.close()
      
    return row

def create_seo_optimized_prompt(distributor_seo_keywords, prompt):
    prompt = f"""
                distributor_seo_keywords: {distributor_seo_keywords},
                prompt: {prompt}
                Perform SEO optimization steps on the given prompt.
                """
    return prompt
    
def get_distributor_info(distributor_id):
    distributor_query = "SELECT * FROM distributor WHERE id = ?"
    distributor_params = (distributor_id,)
    distributor_info_from_database = get_specific_info_from_database(distributor_query, distributor_params)
    return distributor_info_from_database

def get_localmaster_info(local_master_id):
    localMaster_query = "SELECT * FROM localMaster WHERE id = ?"
    localMaster_params = (local_master_id,)
    localMaster_info_from_database = get_specific_info_from_database(localMaster_query, localMaster_params)
    return localMaster_info_from_database
