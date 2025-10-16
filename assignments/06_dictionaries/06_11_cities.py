cities = {
    'baltimore': {
        'country': 'usa',
        'population': 602495,
        'fact': 'Known for its beautiful Inner Harbor and rich maritime history.',
    },
    'tokyo': {
        'country': 'japan',
        'population': 13929286,
        'fact': 'The largest metropolitan area in the world.',
    },
    'paris': {
        'country': 'france',
        'population': 2140526,
        'fact': 'Famous for its art, fashion, and the iconic Eiffel Tower.',
    },
    'new york': {
        'country': 'usa',
        'population': 8419600,
        'fact': 'Known as "The Big Apple" and famous for landmarks like Times Square and Central Park.',
    },
}

for city, details in cities.items():
    country = details['country']
    population = details['population']
    fact = details['fact']
    
    print(f"{city.title()} is in {country.title()}.")
    print(f"It has a population of about {population}.")
    print(f"Fun fact: {fact}\n")