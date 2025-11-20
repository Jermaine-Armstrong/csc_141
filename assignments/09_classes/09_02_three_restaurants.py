class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant1 = Restaurant("Pasta Palace", "Italian")
restaurant2 = Restaurant("Sushi Central", "Japanese")
restaurant3 = Restaurant("Taco Town", "Mexican")
restaurants = [restaurant1, restaurant2, restaurant3]
for restaurant in restaurants:
    restaurant.describe_restaurant()