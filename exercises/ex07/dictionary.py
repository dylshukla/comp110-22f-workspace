"""Dictionaries."""

__author__: str = "730577405"


def invert(stuff: dict[str, str]) -> dict[str, str]:
    """Reverses each key with each value."""
    new: dict[str, str] = {}
    for item in stuff:
        if stuff[item] in new:
            raise KeyError()
        new[stuff[item]] = item
    return new


def favorite_color(stuff: dict[str, str]) -> str:
    """Counts favorite color instances and returns favorite color."""
    favorite: str = ""
    new: list[str] = ()
    i: int = 0
    for colors in stuff:
        new.append(stuff[colors])
    another: dict[str, int] = count(new)
    for color in another:
        if another[color] > i:
            i = another[color]
            favorite = color
    return favorite


def count(idk: list[str]) -> dict[str, int]:
    """Displays number of times each string is displayed."""
    new: dict[str, int] = {}
    i: int = 0
    while i < len(idk):
        if idk[i] in new:
            new[idk[i]] += 1
        else:
            new[idk[i]] = 1
        i += 1
    return new