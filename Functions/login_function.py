from vars import *
def input_username():
    global login_username
    login_username = input("Enter username:     ")
def input_password():
    global login_password
    login_password = input("Enter password:     ")

def log_u():
    if login_username in user_list:
        log_p()
    elif login_username not in user_list:
        print("Username not registered. Try again")
        login()

def log_p():
    input_password()
    if login_password==user_list[login_username]:
        print("Welcome to the library database\n"
        "1. Add a user\n"
        "2. Delete a user\n"
        "3. Check book status\n"
        "4. Check full database\n")
    elif login_password!=user_list[login_username]:
        print("Password incorrect. Try Again")
        log_p()

def login():
    input_username()
    log_u()
