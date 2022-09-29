"""Test file for utils."""

__author__: str = "730577405"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_edge() -> None:
    """Edge case for only_evens."""
    assert only_evens([]) == []


def test_only_evens_1() -> None:
    """First use case for only_evens."""
    assert only_evens([2, 5, 7, 8]) == [2, 8]


def test_only_evens_2() -> None:
    """Second use case to test only_evens."""
    assert only_evens([4, 10, 12]) == [4, 10, 12]


def concat_edge() -> None:
    """Edge case for concat."""
    assert concat([], []) == []


def concat_1() -> None:
    """Use case for concat testing."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def concat_2() -> None:
    """Second use case for concat testing."""
    assert concat([4, 3, 1], [2, 6]) == [4, 3, 1, 2, 6]


def test_sub_edge() -> None:
    """Edge case for sub."""
    assert sub([10, 20, 30, 40], -1, 3) == [10, 20, 30]


def test_sub_1() -> None:
    """First use case for sub."""
    assert sub([5, 10, 15], 1, 2) == [10]


def test_sub_2() -> None:
    """Second use case for testing sub function."""
    assert sub([4, 7, 8, 1, 3], 1, 4) == [7, 8, 1]