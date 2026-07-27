import sqlite3
import os
from variables import Variables
from user import User
from error import UserNotFoundError
db_path = Variables.config.users_db_path

create_users_query = """
CREATE TABLE IF NOT EXISTS Users(
Id Integer PRIMARY KEY AUTOINCREMENT,
Username varchar(255),
Password Text,
CreationDate Text,
PrivilegeLevel Integer
);
"""

create_entries_query = """
CREATE TABLE IF NOT EXISTS Entries(
Id Integer PRIMARY KEY AUTOINCREMENT,
Title Text,
Author Int,
CreationDate Text,
Content Text,
Summary Text
);
"""

insert_user_query = """
INSERT INTO Users(Username, Password, creationDate, PrivilegeLevel) VALUES
(?,?,?,?);
"""

find_user_query = "SELECT * FROM Users WHERE Username = ?;"

grab_hash_query = "SELECT Password FROM Users WHERE Username = ?;"

usersDbFilename = os.path.basename(Variables.config.users_db_path)

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
        q = cur.execute(query)

def add_user(user: object):
    print(f"Inserting user {user.username} into {usersDbFilename}...")
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        params = (user.username, user.password, user.creationDate, user.privilegeLevel)
        q = cur.execute(insert_user_query, (params))
        return(0)

def find_user(username):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        q = cur.execute(find_user_query, (username,))
        session_id = os.urandom(16)
        user = q.fetchone()
        if user == None:
            return UserNotFoundError
        return (0,(user,session_id))

def grab_hash(username):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        q = cur.execute(grab_hash_query, (username,))
        hash = q.fetchone()
        if hash == None:
            return UserNotFoundError
        return hash

if __name__ == "__main__":
    print(create_db(Variables.config.entries_db_path, create_entries_query))