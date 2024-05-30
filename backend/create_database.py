# from core.apps.database_creation_changes import utils
# # Call the upgrade function to create the tables
# utils.update_database_data()

import sqlite3
import os
import json
from core.config import settings

def create_table_schema():

    if os.path.isfile(settings.DB_PATH):
        os.remove(settings.DB_PATH)

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
        
        # Close the connection
        conn.close()

        print("Record added successfully.")

def create_database():
    try:
        create_table_schema()
        add_market_record()
        add_distributor_record()
        return True
    except Exception as e:
        print(e)
        return False
    
if __name__ == "__main__":
    create_database()