from register import register
from data import create_db
from login import login
from variables import Variables

#create_db(Variables.config.users_db_path)

print(register("Toby", "Pwd987Toby@"))
print("Login: ",login("Toby", "Pwd987Toby@"))