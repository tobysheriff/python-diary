from user import list_users, find_user
from entries import get_entries

class Menu:
    def __init__(self, title, selection):
        self.title = title
        self.selection = selection 

    def __str__(self):
        body = ""
        for i, v in enumerate(self.selection):
            body += (f"[{i}] {v}\n")
        menu = f"--- {self.title} ---\n{body}"
        return menu

def display_users(users):
    string = ""
    for user in users:
        string += (f"{user[0]}: {user[1]}\n")
    return string

def user_menu(id, data):
    user_menu = Menu(
        f"Options for {data[1]}",
        ["Create Entry", "View Entries", "Change Password", "Change Username", "Remove Account"]
    )
    print(user_menu)

def home_menu():
    menu="""
--- Admin Menu ---
Select a user
"""
    print(menu)
    print(display_users(list_users()))
    selectedId = input(">")
    userData = find_user(selectedId)[1][0]
    user_menu(selectedId, userData)
if __name__ == "__main__":
    home_menu()