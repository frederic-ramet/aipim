

# from core.apps.database_creation_changes import utils
# # Call the upgrade function to create the tables
# utils.update_database_data()

import sqlite3
import os
import json
from core.config import settings

def create_table_schema(conn):

    if os.path.isfile(settings.DB_PATH):
        os.remove(settings.DB_PATH)

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
            titleRecommendations VARCHAR(100),
            label VARCHAR(100),
            descRecommendations VARCHAR(100),
            tone VARCHAR(100),
            target VARCHAR(100),
            seoKeywords VARCHAR(100),
            created_at DATETIME
        )
    ''')

    # Create 'market' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS market (
            id INTEGER PRIMARY KEY,
            label VARCHAR(100),
            features VARCHAR(100),
            marketingAxis VARCHAR(100),
            languages VARCHAR(100),
            trends VARCHAR(100),
            seoKeywords VARCHAR(100),
            created_at DATETIME
        )
    ''')

    # Create 'configurations' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS configurations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            config_name VARCHAR(100) UNIQUE,
            config_data TEXT,
            created_at DATETIME
        )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()

def add_market_record(conn):
   
    # Define the data to be inserted
    with open("static/parameters/market.json", 'r') as file:
        data = json.load(file)
    
    for key in data:
        record = data[key]
        cursor = conn.cursor()
        
        # SQL command for inserting a new record
        sql = '''
            INSERT INTO market (id, label, marketingAxis, trends, languages, seoKeywords, features, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
        '''
        # Execute the SQL command
        cursor.execute(sql, (
            record['id'],
            str(record['label']),
            str(record['marketingAxis']),
            str(record['trends']),
            str(record['languages']),
            str(record['seoKeywords']),
            str(record['features'])
            ))
        
        # Commit the changes
        conn.commit()
        

        print("Record added successfully.")

def add_distributor_record(conn):
    # Define the data to be inserted
    with open("static/parameters/distributors.json", 'r') as file:
        data = json.load(file)

    for key in data:
        record = data[key]

        cursor = conn.cursor()
        
        # SQL command for inserting a new record
        sql = '''
            INSERT INTO distributor (titleRecommendations, label, descRecommendations, tone, target, seoKeywords, id, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
        '''
        
        # Execute the SQL command
        cursor.execute(sql, (
            record['titleRecommendations'],
            record['label'],
            record['descRecommendations'],
            record['tone'],
            record['target'],
            str(record['seoKeywords']),
            record['id'],
        ))

        # Commit the changes
        conn.commit()
        

        print("Record added successfully.")


def create_database(): 
    try:
        conn = sqlite3.connect(settings.DB_PATH)
        create_table_schema(conn)
        add_market_record(conn)
        add_distributor_record(conn)
        # Close the connection
        conn.close()

        return True
    except Exception as e:
        print(e)
        return False
    
def update_configuration_database(config_name):
    conn = sqlite3.connect(settings.DB_PATH)

    config_data = {}
    directory = "static/parameters"
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
             with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                config_data[filename] = json.load(file)    
    conn = sqlite3.connect(settings.DB_PATH)
    cursor = conn.cursor()

    # SQL command for inserting a new configuration
    sql = '''
        INSERT INTO configurations (config_name, config_data, created_at)
        VALUES (?, ?, datetime('now'))
    '''

    try:
        # Execute the SQL command
        cursor.execute(sql, (config_name, json.dumps(config_data, ensure_ascii=False)))
        
        # Commit the changes
        conn.commit()
        print("Configuration added successfully.")

        # Empty the tables 'market' and 'distributor'
        try:
            cursor.execute("DELETE FROM market;")
            cursor.execute("DELETE FROM distributor;")
            print("Tables emptied successfully.")
        except sqlite3.Error as e:
            print(f"Error when trying to empty tables: {e}")

        try:
            add_market_record(conn)
            add_distributor_record(conn)
        except Exception as e:
            print(f"Error when populating tables: {e}")


    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        conn.close()
    



if __name__ == "__main__":
    create_database()