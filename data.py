import sqlite3
import os
from variables import Variables

create_users_query = """
CREATE TABLE IF NOT EXISTS Users(
Id Integer PRIMARY KEY AUTOINCREMENT,
Username varchar(255),
Password Text,
CreationDate Text,
PrivilegeLevel Integer
)
"""

def remove_exisiting_db(path):
    if os.path.exists(path):
        os.remove(path)
        return 0

def clear_data_directory():
    os.removedirs("./data")
    os.makedirs("./data")

def create_db(path):
    print("Creating")
    with sqlite3.connect(path) as conn:
        cur = conn.cursor()
        q = cur.execute(create_users_query)
        print(q)

def add_user(user: object):
    

if __name__ == "__main__":
    create_db(Variables.config.users_db_path)