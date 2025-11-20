import json
import os

def get_stored_username(filename):
    """Return the stored username if available."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            username = json.load(f)
        return username
    return None

def get_new_username(filename):
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    with open(filename, "w") as f:
        json.dump(username, f)
    return username

def greet_user(filename):
    """Greet the user, verifying if it's the correct username."""
    username = get_stored_username(filename)
    if username:
        answer = input(f"Are you {username}? (yes/no) ").strip().lower()
        if answer != 'yes':
            username = get_new_username(filename)
            print(f"We'll remember you, {username}!")
        else:
            print(f"Welcome back, {username}!")
    else:
        username = get_new_username(filename)
        print(f"We'll remember you, {username}!")

filename = "username.json"
greet_user(filename)
