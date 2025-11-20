import json

filename = "favorite_number.json"

favorite_number = input("What is your favorite number? ")

with open(filename, "w") as f:
    json.dump(favorite_number, f)

print("Your favorite number has been saved!")

import json

filename = "favorite_number.json"

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    print("I couldn't find your favorite number file.")
else:
    print(f"I know your favorite number! It's {favorite_number}.")
