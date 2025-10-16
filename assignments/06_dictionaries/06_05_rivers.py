rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'mississippi': 'united states',
    'danube': 'europe',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")