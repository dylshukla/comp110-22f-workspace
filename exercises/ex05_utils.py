""""""

__author__: str = "730577405"

def only_evens(x: list[int]) -> list[int]:
    i: int = 0
    y: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            y.append(x[i])
        i+= 1
    return y


def concat(x: list[str], y: list[str]) -> list[str]:
    z: list[str] = []
    z.append(x)
    z.append(y)
    return z