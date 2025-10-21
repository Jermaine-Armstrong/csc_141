current_topping = "pepperoni"
while current_topping != "quit":
    print(f"Adding {current_topping} to your pizza.")
    current_topping = input("Enter a pizza topping (or 'quit' to finish): ")
print("Finished making your pizza!")