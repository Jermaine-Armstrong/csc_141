person1 = {
    'first_name': 'Naiyah',
    'last_name': 'Johnson',
    'age': 17,
    'city': 'New York',
}

person2 = {
    'first_name': 'Jermaine',
    'last_name': 'Armstrong',
    'age': 18,
    'city': 'Baltimore',
}   

person3 = {
    'first_name': 'Shania',
    'last_name': 'Brandon',
    'age': 19,
    'city': 'Chicago',
}

people = [person1, person2, person3]
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"{full_name}, Age: {age}, City: {city}")