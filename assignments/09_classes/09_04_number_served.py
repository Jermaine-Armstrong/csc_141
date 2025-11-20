class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, additional_customers):
        if additional_customers > 0:
            self.number_served += additional_customers
        else:
            print("Additional customers must be positive.")

restaurant = Restaurant("The Gourmet Kitchen", "International")

print(f"Initial number of customers served: {restaurant.number_served}")

restaurant.number_served = 25
print(f"Updated number of customers served: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Set number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(30)
print(f"Incremented number of customers served: {restaurant.number_served}")