age = input ("How old are you? ")

if age.lower () == 'quit':
    print ("Goodbye!")
else:
    age = int (age)
    if age < 5:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15

    print (f"Your movie ticket price is ${price}.")