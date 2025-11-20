print("Give me two numbers and I'll add them together.")

first_number = input("First number: ")
second_number = input("Second number: ")

try:
        answer = int(first_number) + int(second_number)
except ValueError:
        print("Invalid input. Please enter numeric values.")
else:
        print(f"The sum of {first_number} and {second_number} is {answer}.")