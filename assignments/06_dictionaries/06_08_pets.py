pet1 = {
    'name': 'whiskers',
    'type': 'cat',
    'owner': 'alice',
}

pet2 = {
    'name': 'buddy',
    'type': 'dog',
    'owner': 'bob',
}

pet3 = {
    'name': 'tweety',
    'type': 'bird',
    'owner': 'carol',
}

pets = [pet1, pet2, pet3]
for pet in pets:
    name = pet['name']
    pet_type = pet['type']
    owner = pet['owner']
    print(f"{name.title()} is a {pet_type} owned by {owner.title()}.")