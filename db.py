import sqlite3
import os
from variables import Variables

def remove_exisiting_db(path):
    if os.path.exists(path):
        os.remove(path)
        return 0

def clear_data_directory():
    os.removedirs("./data")
    os.makedirs("./data")

def create_db(path,query):
    print("Creating")
    with sqlite3.connect(path) as conn:
        cur = conn.cursor()
        cur.execute(query)

if __name__ == "__main__":
    print(create_db(Variables.config.entries_db_path, 
    """
        CREATE TABLE IF NOT EXISTS Entries(
        Id Integer PRIMARY KEY AUTOINCREMENT,
        Title Text,
        Author Int,
        CreationDate Text,
        Content Text,
        Summary Text
        );
    """))
    
    print(create_db(Variables.config.users_db_path, 
        """
        CREATE TABLE IF NOT EXISTS Users(
        Id Integer PRIMARY KEY AUTOINCREMENT,
        Username varchar(255),
        Password Text,
        CreationDate Text,
        PrivilegeLevel Integer
        );
    """
))