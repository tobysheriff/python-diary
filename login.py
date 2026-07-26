import sqlite3
import bcrypt
from variables import Variables
from data import grab_hash
users_path = Variables.config.users_db_path

def login(username, password):
    grab_hash(username)
    