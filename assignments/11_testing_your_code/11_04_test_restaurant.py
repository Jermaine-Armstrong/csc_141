import pytest

from restaurant import Restaurant


@pytest.fixture
def diner():
    """Provide a fresh Restaurant instance for each test."""
    return Restaurant("Tasty Treats", "fusion")


def test_initial_attributes(diner):
    assert diner.name == "Tasty Treats"
    assert diner.cuisine_type == "fusion"
    assert diner.number_served == 0


def test_describe_restaurant_prints_name_and_cuisine(diner, capsys):
    diner.describe_restaurant()
    captured = capsys.readouterr()
    assert "Tasty Treats" in captured.out
    assert "fusion" in captured.out


def test_open_restaurant_message(diner, capsys):
    diner.open_restaurant()
    captured = capsys.readouterr()
    assert "now open" in captured.out.lower()
