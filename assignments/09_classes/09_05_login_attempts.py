class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("YungPrahfit", "jarmstrong@example.com")
user.describe_user()
user.greet_user()

print(f"Initial login attempts: {user.login_attempts}")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts after incrementing: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts after resetting: {user.login_attempts}")