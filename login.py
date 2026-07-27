import secrets
import bcrypt
from variables import Variables
from data import grab_hash, find_user
import os
users_path = Variables.config.users_db_path

def login(username, password:str):
    hpass = password.encode("utf-8")
    hash = grab_hash(username)[0]
    if bcrypt.checkpw(hpass, hash):
        data = find_user(username)
        return data


if __name__ == "__main__":
    login("Toby")