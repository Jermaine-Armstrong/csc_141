import importlib.util
from pathlib import Path

import pytest


def _load_module():
    """Load the 11_02_population.py module even though its name starts with a digit."""
    path = Path(__file__).with_name("11_02_population.py")
    spec = importlib.util.spec_from_file_location("city_module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


@pytest.fixture(scope="module")
def city_mod():
    return _load_module()


def test_city_country_basic(city_mod):
    assert city_mod.city_country("santiago", "chile") == "Santiago, Chile"


def test_city_country_with_population(city_mod):
    result = city_mod.city_country("santiago", "chile", population=5_000_000)
    assert result == "Santiago, Chile – population 5000000"
