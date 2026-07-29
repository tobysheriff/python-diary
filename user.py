import sqlite3
import os
from variables import Variables
from error import UserNotFoundError

class User:
    def __init__(self, username:str, password:str, creationDate:int, privilegeLevel:int):
        self.username = username
        self.password = password
        self.creationDate = creationDate
        self.privilegeLevel = privilegeLevel

users_db = Variables.config.users_db_path

def add_user(user: object):
    filename = os.path.basename(users_db)
    print(f"Inserting user {user.username} into {filename}...")
    with sqlite3.connect(users_db) as conn:
        cur = conn.cursor()
        params = (user.username, user.password, user.creationDate, user.privilegeLevel)
        cur.execute("""
        INSERT INTO Users(Username, Password, creationDate, PrivilegeLevel) VALUES
        (?,?,?,?);
        """, (params))
        return 0

def get_id(username):
    with sqlite3.connect(users_db) as conn:
        cur = conn.cursor()
        q = cur.execute("SELECT Id from Users WHERE Username = ?;", (username,))
        return q.fetchone

def find_user(id):
    with sqlite3.connect(users_db) as conn:
        cur = conn.cursor()
        q = cur.execute("SELECT * FROM Users WHERE Id = ?;", (id,))
        session_id = os.urandom(16)
        user = q.fetchone()
        if user == None:
            return UserNotFoundError
        return (0,(user,session_id))

def grab_hash(id):
    with sqlite3.connect(users_db) as conn:
        cur = conn.cursor()
        q = cur.execute("SELECT Password FROM Users WHERE Id = ?;", (id,))
        hash = q.fetchone()
        if hash == None:
            return UserNotFoundError
        return hash

def remove_user(id):
    with sqlite3.connect(users_db) as conn:
        cur = conn.cursor()
        q = cur.execute("DELETE FROM Users WHERE id = ?;", (id,))
        return q

def list_users():
    with sqlite3.connect(users_db) as conn:
        cur = conn.cursor()
        q = cur.execute("SELECT Id, Username FROM USERS")
        return q.fetchall()