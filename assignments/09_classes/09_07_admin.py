class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Profile:")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Age: {self.age}")
        print(f" Email: {self.email}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name} {self.last_name}!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can reset passwords",
        ]

    def show_privileges(self):
        print(f"\nAdministrator Privileges for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_user = Admin("Jermaine", "Armstrong", 18, "jarmstrong3@example.com")

admin_user.describe_user()
admin_user.show_privileges()
