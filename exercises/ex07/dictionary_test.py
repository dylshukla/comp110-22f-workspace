"""Testing file for dictionary file."""

__author__: str = "730577405"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_edge() -> None:
    """Edge case for invert function"""
    assert invert({}) == {}


def test_invert_use_1() -> None:
    """First use case for invert."""
    assert invert({'y': 'f', 'x': 's', 'w': 'q'}) == {'f': 'y', 's': 'x', 'q': 'w'}


def test_invert_use_2() -> None:
    """Second use case for invert."""
    assert invert({'t': 'w', 'q': 'z', 'a': 'h'}) == {'w': 't', 'z': 'q', 'h': 'a'}


def test_favorite_color_edge() -> None:
    """Edge case for favorite color function."""
    assert favorite_color({}) == {}


def test_favorite_color_use_1() -> None:
    """Use case 1 for favorite color."""
    assert favorite_color({"Dylan": "green", "Samir": "red", "Luis": "red"}) == "red"


def test_favorite_color_use_2() -> None:
    """Second use case for favorite color."""
    assert favorite_color({"Pranav": "green", "Samir": "green", "Luis": "red"}) == "green"


def test_count_edge() -> None:
    """Edge case for count function."""
    assert count(["a", "b", "c"]) == {'a': 2, 'b': 1}


def test_count_use_1() -> None:
    """First use case for count function."""
    assert count(["a", "b", "a"]) == {'a': 2, 'b': 1}


def test_count_use_2() -> None:
    """Second use case for count function."""
    assert count(["a", "b", "b"]) == {'a': 1, 'b': 2}