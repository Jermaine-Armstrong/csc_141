current_users = ['admin', 'd1kendall', 'kamthegreat', 'yungprahfit', 'chas1ingpape']
new_users = ['D1Kendall', 'KamTheGreat', 'newuser', 'anotheruser', 'yungprahfit']
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"Username '{new_user}' is available.")