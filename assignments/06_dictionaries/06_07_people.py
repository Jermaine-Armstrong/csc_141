person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
}

person2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles',
}   

person3 = {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'Chicago',
}

people = [person1, person2, person3]
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"{full_name}, Age: {age}, City: {city}")