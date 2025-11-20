filename = "guest.txt"

name = input("Please enter your name: ")
with open(filename, 'w') as file_object:
    file_object.write(name + '\n')
print(f"Hello, {name}! Your name has been recorded in {filename}.")