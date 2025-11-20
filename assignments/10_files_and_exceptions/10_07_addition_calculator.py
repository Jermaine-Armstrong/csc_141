print("Give me two numbers and I'll add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        print(f"The sum of {first_number} and {second_number} is {answer}.")