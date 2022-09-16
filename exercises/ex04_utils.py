"""Lists."""

__author__: str = "730577405"


def all(nums: list[int], num: int) -> bool:
    """Checks if list numbers are all same as provided int."""
    i: int = 0
    isFalse: bool = True
    while i < len(nums):
        if num == nums[i]:
            i += 1
        else:
            return False
    if len(nums) == 0:
        return False
    elif i == len(nums):
        isFalse = True
    return isFalse


def max(input: list[int]) -> int:
    """Returns largest number of list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    j: int = 0
    m: int = input[0]
    while j < len(input):
        if input[j] > m:
            m = input[j]
        j += 1
    return m


def is_equal(first: list[int], second: list[int]) -> bool:
    """Checks for deep equality between two lists."""
    k: int = 0
    isTrue: bool = False
    if len(first) != len(second):
        return False
    while k < len(first):
        if first[k] == second[k]:
            k += 1
        else:
            return False
    if k == len(first):
        isTrue = True
    return isTrue