def city_country(city, country):
    """Return a string in the format 'City, Country'."""
    return f"{city.title()}, {country.title()}"


if __name__ == "__main__":
    for c, n in [("santiago", "chile"), ("paris", "france"), ("tokyo", "japan"), ("new york", "united states")]:
        print(city_country(c, n))
