class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print(f"{self.name} offers the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Sweet Treats")
ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.add_flavor("Chocolate")
ice_cream_stand.add_flavor("Strawberry")
ice_cream_stand.display_flavors()