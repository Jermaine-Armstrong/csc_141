class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"User Profile:")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Age: {self.age}")
        print(f" Email: {self.email}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name} {self.last_name}!\n")


user1 = User("Jermaine", "Armstrong", 17, "jarmstrong3@example.com")
user2 = User("Kamerin", "Nash", 19, "knash@example.com")
user3 = User("Kendall", "Hazard", 19, "khazard@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
