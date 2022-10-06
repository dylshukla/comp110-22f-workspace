"""Utils file for function definitons."""

__author__: str = "730577405"


def only_evens(x: list[int]) -> list[int]:
    """Returns all even in list."""
    i: int = 0
    y: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            y.append(x[i])
        i += 1
    return y


def concat(x: list[str], y: list[str]) -> list[str]:
    """Combines two lists."""
    z: list[str] = []
    i: int = 0
    j: int = 0
    while i < len(x):
        z.append(x[i])
        i += 1
    while j < len(y):
        z.append(y[j])
        j += 1
    return z


def sub(x: list[int], si: int, ei: int) -> list[int]:
    """Returns values of list within given intervals."""
    y: list[int] = []
    if si > len(x) or ei <= 0:
        return y
    if si < 0:
        si = 0
    if ei > len(x):
        ei = len(x)
    if si >= 0 and ei <= len(x):
        while si < ei:
            y.append(x[si])
            si += 1
        return y