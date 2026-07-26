import sqlite3
import os
from variables import Variables
from user import User

create_users_query = """
CREATE TABLE IF NOT EXISTS Users(
Id Integer PRIMARY KEY AUTOINCREMENT,
Username varchar(255),
Password Text,
CreationDate Text,
PrivilegeLevel Integer
)
"""

insert_user_query = """
INSERT INTO Users(Username, Password, creationDate, PrivilegeLevel) VALUES
(?,?,?,?)
"""

find_user_query = "SELECT * FROM Users WHERE Username = ?"

grab_hash_query = "SELECT Hash FROM Users WHERE Username = ?"

usersDbFilename = os.path.basename(Variables.config.users_db_path)

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
    print(f"Inserting user {user.username} into {usersDbFilename}...")
    with sqlite3.connect(Variables.config.users_db_path) as conn:
        cur = conn.cursor()
        params = (user.username, user.password, user.creationDate, user.privilegeLevel)
        q = cur.execute(insert_user_query, (params))
        return(q)

def find_user(username):
    with sqlite3.connect(Variables.config.users_db_path) as conn:
        cur = conn.cursor()
        q = cur.execute(find_user_query, (username,))
        return(q.fetchone())

def grab_hash(username):
    with sqlite3.connect(Variables.config.users_db_path) as conn:
        cur = conn.cursor()
        q = cur.execute(grab_hash_query, (username,))
        return(q.fetchone())
    
if __name__ == "__main__":
    find_user("Toby")