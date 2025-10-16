favorite_places = {
    'alice': ['paris', 'new york'],
    'bob': ['tokyo'],
    'carol': ['london', 'berlin', 'rome'],
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")