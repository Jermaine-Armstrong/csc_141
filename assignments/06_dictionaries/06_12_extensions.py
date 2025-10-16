cities = {
    'baltimore': {
        'country': 'usa',
        'population': 602495,
        'fact': 'Known for its beautiful Inner Harbor and rich maritime history.',
        'landmarks': ['Inner Harbor', 'Fort McHenry', 'National Aquarium'],
        'year_founded': 1729,
    },
    'tokyo': {
        'country': 'japan',
        'population': 13929286,
        'fact': 'The largest metropolitan area in the world.',
        'landmarks': ['Tokyo Tower', 'Shibuya Crossing', 'Meiji Shrine'],
        'year_founded': 1603,
    },
    'paris': {
        'country': 'france',
        'population': 2140526,
        'fact': 'Famous for its art, fashion, and the iconic Eiffel Tower.',
        'landmarks': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'],
        'year_founded': 508,
    },
    'new york': {
        'country': 'usa',
        'population': 8419600,
        'fact': 'Known as "The Big Apple" and famous for landmarks like Times Square and Central Park.',
        'landmarks': ['Statue of Liberty', 'Times Square', 'Central Park'],
        'year_founded': 1624,
    },
}

for city, details in cities.items():
    country = details['country']
    population = details['population']
    fact = details['fact']
    landmarks = details['landmarks']
    year_founded = details['year_founded']
    
    print(f"{city.title()} is in {country.title()}.")
    print(f"It has a population of about {population}.")
    print(f"Fun fact: {fact}")
    print(f"Famous landmarks include: {', '.join(landmarks)}.")
    print(f"It was founded in the year {year_founded}.\n")