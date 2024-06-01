import sqlite3
import json

from core.config import settings


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
    db.execute(query, parameter)

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


def insert_info_to_database(distributorVersion_title, distributorVersion_distributor, distributorVersion_distributorId,
                            distributorVersion_settings, distributorVersion_prompt, distributorVersion_content,
                            distributorVersion_localMasterId):
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


def distributor_prompt_generator(distributor_info_from_database: dict, localMaster_info_from_database: dict,
                                 distributor_settings: str):
    distributor_data_dict = eval(distributor_settings)
    distributor_label = distributor_data_dict['label']
    distributor_title_recom = distributor_data_dict['titleRecommendations']
    distributor_desc_recom = distributor_data_dict['descRecommendations']
    distributor_distribution = distributor_data_dict["description"]
    distributor_tone = distributor_data_dict["tone"]
    distributor_language = distributor_data_dict["language"]
    distributor_target = distributor_data_dict["target"]
    distributor_seo_keywords = distributor_data_dict["seoKeywords"]
    generated_content = localMaster_info_from_database["content"]

    prompt_json_path = settings.PROMPT_MASTER_JSON_PATH
    with open(prompt_json_path, 'r') as file:
        data = json.load(file)
    prompt_template_prefix  = data.get('distributor_sheet', {}).get('prompt')
    prompt_template_context = data.get('distributor_sheet', {}).get('prompt_context')

    variables = {
        "distributor_label": distributor_data_dict['label'],
        "localMaster_title": localMaster_info_from_database['title'],
        "distributor_title_recom": distributor_data_dict['titleRecommendations'],
        "distributor_desc_recom": distributor_data_dict['descRecommendations'],
        "distributor_target": distributor_data_dict["target"],
        "distributor_tone": distributor_data_dict["tone"],
        "distributor_distribution": distributor_data_dict["description"],
        "distributor_seo_keywords": ", ".join(distributor_data_dict["seoKeywords"]),
        "distributor_language": distributor_data_dict["language"],
        "generated_content": localMaster_info_from_database["content"]
    }

    prompt_prefix = prompt_template_prefix.format(**variables)
    prompt_context = prompt_template_context.format(**variables)
    
    '''
    # insert_generated_prompt_database(prompt, distributor_info_from_database, localMaster_info_from_database, distributor_settings)
    prompt_prefix = f"""
    Role:
    You are a content writer working at Nexans. 
    Your mission is to write product marketing content providing an overview of the various types of cables offered by Nexans, along with their primary applications. 

    Task:
    Generate a product content for the specific distributor of "{clear}".

    Context: 
    You will provided by a list of information about a Nexans's product, you need to use them in the content generation.
    The context is provided inside <context></context> tags.

    Process: 
    - use the provided context to adapt the generated content (mentioned in <localMaster_info>), generated for as local product content for the product "{localMaster_info_from_database['title']}".
    - generate a product marketing content for the distributor of "{distributor_label}".
    - the generated title must respect these recommendations: {distributor_title_recom}
    - the generated description must respect these recommendations: {distributor_desc_recom}
    - the content must be adapted for these type of market "{distributor_target}".
    - adapte the content according to the <distributor_tone>.
    - don't forget to use the distributor data from {distributor_distribution}.
    - optimise the content for the SEO and use the keywords mentioned in {distributor_seo_keywords}.
    - the content must be written in {distributor_language}

    Output:
    - the generated content must provide at least:
        - a well written title
        - short description
        - product marketing content
    - the output must be written in {distributor_language}
    - the output must be formatted en HTML.
    - remove all the "\n" and any json formatting

    """
    prompt_context = f"""
    <context>
    <distributor_distribution>{distributor_distribution}</distributor_distribution>
    <localMaster_info>{generated_content}</localMaster_info>
    <distributor_tone>{distributor_tone}</<distributor_tone>
    <seo_keywords>{distributor_seo_keywords}</seo_keywords>
    </context>
    """
    '''
    prompt = f"""{prompt_prefix} {prompt_context}"""

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


def distributer_versions_list(localMasterId: int):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute("SELECT * FROM distributorVersion WHERE localMasterId = ?", (localMasterId,))

    # Fetch the first matching row
    row = db.fetchall()

    # Check if any rows were fetched
    if row:
        print("Data fetch successfully.")
    else:
        print("No data found with localMasterId:", localMasterId)

    # Close the connection
    conn.close()

    return row

def get_one_distributor_version_from_database(id):
    conn = sqlite3.connect('ai-pim.db')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # SQL command to fetch the first row where the title is 'XYZ'
    db.execute("SELECT * FROM distributorVersion WHERE id = ?", (id,))

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