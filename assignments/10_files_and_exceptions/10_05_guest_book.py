filename = "guest_book.txt"

print("Enter your name or type 'q' at any time to quit.")

while True:
    name = input("Please enter your name: ")
    if name.lower() == 'q':
        print("Thank you for visiting the guest book. Goodbye!")
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + '\n')
        print(f"Hello, {name}! Your name has been added to the guest book.")