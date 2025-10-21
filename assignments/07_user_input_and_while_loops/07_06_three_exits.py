topping = ""
while topping != "quit":
    topping = input("Enter a topping for your pizza (or 'quit' to stop): ")
    if topping != "quit":
        print("Adding {topping} to your pizza.")
print("Finished making your pizza!")

while True:
    topping = input("Enter a topping for your pizza (or 'quit' to stop): ")
    if topping == "quit":
        break
    print("Adding {topping} to your pizza.")
print("Finished making your pizza!")

active = True
while active:
    topping = input("Enter a topping for your pizza (or 'quit' to stop): ")
    if topping == "quit":
        active = False
    else:
        print("Adding {topping} to your pizza.")
print("Finished making your pizza!")