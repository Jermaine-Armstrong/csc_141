def city_country(city, country, population=None):
    """Return a string like 'City, Country' or 'City, Country – population xxx'."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" – population {population}"
    return result

def test_city_country():
    """Test function without population."""
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

def test_city_country_population():
    """Test function with population."""
    result = city_country('santiago', 'chile', population=5000000)
    assert result == 'Santiago, Chile – population 5000000'
