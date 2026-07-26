import sqlite3
import os
from variables import Variables

create_users_query = """
CREATE TABLE IF NOT EXISTS Users(
Id Integer PRIMARY KEY AUTOINCREMENT,
Username varchar(255),
Password Text,
CreationDate Text,
PrivilegeLevel Text,
Banned Text
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


if __name__ == "__main__":
    print("You've run me as a script!")