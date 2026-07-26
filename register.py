import sqlite3
from variables import Variables
from user import User
import datetime
import bcrypt

users_db = Variables.config.users_db

def register(username, password):
    #Check if username exists
    with sqlite3.connect(users_db) as conn:
        cur = conn.cursor()
        q = cur.execute("SELECT 1 FROM Users WHERE Username = ?", username)
        if q.fetchone():
            return (1,"User already exists")
    valid_password = password_check(password_check)
    if valid_password[0] == False:
        return (1, valid_password[1])
    else: 
        hash = hash_password(password)
        user = User(username, hash, datetime.datetime.now, 2)
        
def hash_password(password):
    pw = bytes(password)
    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(pw, salt)
    return hash

def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        message = 'Length should be at least 6'
        val = False
    if len(passwd) > 20:
        message = 'Length should not be greater than 20'
        val = False

    # Flags for each condition
    has_digit = has_upper = has_lower = has_sym = False

    for char in passwd:
        if 48 <= ord(char) <= 57:
            has_digit = True
        elif 65 <= ord(char) <= 90:
            has_upper = True
        elif 97 <= ord(char) <= 122:
            has_lower = True
        elif char in SpecialSym:
            has_sym = True

    if not has_digit:
        message = 'Password should have at least one numeral'
        val = False
    if not has_upper:
        message = 'Password should have at least one uppercase letter'
        val = False
    if not has_lower:
        message = 'Password should have at least one lowercase letter'
        val = False
    if not has_sym:
        message = 'Password should have at least one of the symbols $@#%'
        val = False

    return (val, message)
