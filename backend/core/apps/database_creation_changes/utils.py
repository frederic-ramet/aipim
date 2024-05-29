import sqlite3
import os
import json
from core.config import settings


def update_json_file_in_static(json_path, json_data):
    with open(json_path, 'w') as fp:
        json.dump(json_data, fp)


def check_json_structure(json_str_data):
    print(json_str_data)
    try:
        parsed_json = eval(json_str_data)

        print("parsed_json::: ", parsed_json)
        print(type(parsed_json))
        if isinstance(parsed_json, dict):
            return parsed_json
        else:
            return False
    except json.JSONDecodeError:
        return False


def check_distributor_json_structure(json_str_data):
    distributor_original_key_list = sorted(
        ["Id", "Label", "Title", "Description", "Main target", "Seo keywords", "Tone"])

    try:
        parsed_json = eval(json_str_data)
        print("~~ ~~ " * 20)
        for key in parsed_json.keys():
            print(parsed_json[key].keys())
            if sorted(parsed_json[key].keys()) == distributor_original_key_list:
                return True
            else:
                return False
    except json.JSONDecodeError:
        return False


def check_market_json_structure(json_str_data):
    market_original_key_list = sorted(
        ["Id", "Title", "Marketing_axis", "Cultural_recommendations", "Languages", "SEO_keywords", "Market_features"])

    try:
        parsed_json = eval(json_str_data)
        print("~~ ~~ " * 20)
        for key in parsed_json.keys():
            print(parsed_json[key].keys())
            if sorted(parsed_json[key].keys()) == market_original_key_list:
                return True
            else:
                return False
    except json.JSONDecodeError:
        return False


def check_product_json_structure(json_str_data):
    product_original_key_list = sorted(["Title", "Description", "Features_1", "features_2", "features_3", "Url"])

    try:
        parsed_json = eval(json_str_data)
        print("~~ ~~ " * 20)
        for key in parsed_json.keys():
            print(parsed_json[key].keys())
            if sorted(parsed_json[key].keys()) == product_original_key_list:
                return True
            else:
                return False
    except json.JSONDecodeError:
        return False


def upgrade():
    # os.remove(settings.DB_PATH)

    conn = sqlite3.connect(settings.DB_PATH)
    cursor = conn.cursor()

    # Create 'masterProduct' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS masterProduct (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(100),
            url VARCHAR(100),
            description VARCHAR(100) UNIQUE,
            features VARCHAR(100),
            content VARCHAR(100),
            created_at DATETIME
        )
    ''')

    # Create 'localMaster' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS localMaster (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(100),
            marketName VARCHAR(100),
            marketId INTEGER NOT NULL,
            settings VARCHAR(100),
            prompt VARCHAR(100),
            content VARCHAR(100),
            masterProductId INTEGER,
            created_at DATETIME,
            FOREIGN KEY (masterProductId) REFERENCES masterProduct(id)
        )
    ''')

    # Create 'distributorVersion' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS distributorVersion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(100),
            distributor VARCHAR(100),
            distributorId INTEGER NOT NULL,
            settings VARCHAR(100),
            prompt VARCHAR(100),
            content VARCHAR(100),
            localMasterId INTEGER,
            created_at DATETIME,
            FOREIGN KEY (localMasterId) REFERENCES localMaster(id)
        )
    ''')

    # Create 'distributor' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS distributor (
            id INTEGER PRIMARY KEY,
            title VARCHAR(100),
            label VARCHAR(100),
            description VARCHAR(100),
            defaultSettings VARCHAR(100),
            tone VARCHAR(100),
            format VARCHAR(100),
            seoKeywords VARCHAR(100),
            created_at DATETIME,
            FOREIGN KEY (id) REFERENCES distributorVersion(distributorId)
        )
    ''')

    # Create 'market' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS market (
            id INTEGER PRIMARY KEY,
            title VARCHAR(100),
            defaultSettings VARCHAR(100),
            marketFeatures VARCHAR(100),
            defaultAxis VARCHAR(100),
            languages VARCHAR(100),
            culturalTrends VARCHAR(100),
            seoKeywords VARCHAR(100),
            created_at DATETIME,
            FOREIGN KEY (id) REFERENCES localMaster(marketId)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def add_market_record():
    # Define the data to be inserted
    with open("static/parameters/market.json", 'r') as file:
        data = json.load(file)

    for key in data:
        record = data[key]
        # Connect to the SQLite database
        conn = sqlite3.connect(settings.DB_PATH)
        cursor = conn.cursor()

        # SQL command for inserting a new record
        sql = '''
            INSERT INTO market (title, defaultSettings, defaultAxis, languages, culturalTrends, seoKeywords, created_at, id, marketFeatures)
            VALUES (?, ?, ?, ?, ?, ?, datetime('now'), ?, ?)
        '''

        # Execute the SQL command
        cursor.execute(sql, (
            record['Title'],
            "",
            str(record['Marketing_axis']),
            str(record['Languages']),
            record['Cultural_recommendations'],
            str(record['SEO_keywords']),
            record['Id'],
            str(record['Market_features'])
        ))

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

        print("Record added successfully.")


def add_distributor_record():
    # Define the data to be inserted
    with open("static/parameters/distributors.json", 'r') as file:
        data = json.load(file)

    for key in data:
        record = data[key]
        # Connect to the SQLite database
        conn = sqlite3.connect(settings.DB_PATH)
        cursor = conn.cursor()

        # SQL command for inserting a new record
        sql = '''
            INSERT INTO distributor (title ,label ,description ,defaultSettings ,tone ,format ,seoKeywords ,id, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
        '''

        # Execute the SQL command
        cursor.execute(sql, (
            record['Title'],
            record['Label'],
            record['Description'],
            "",
            record['Tone'],
            record['Main target'],
            str(record['Seo keywords']),
            record['Id'],
        ))

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

        print("Record added successfully.")


def update_database_data():
    try:
        upgrade()
        add_market_record()
        add_distributor_record()
        return True
    except Exception as e:
        print(e)
        return False
