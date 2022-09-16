"""Example implementing a list utility function."""

# functino name contains
# 2 parameters: needle(str) and haystack (list[str])
# return type bool
def contains(needle: str, haystack: list[str]) -> bool:
    # 1. start with first index
    i: int = 0
    # 2. loop through every index
    while i < len(haystack):
        # 1. A test if item at index equal to needle
        if haystack[i] == needle:
            return True
        # 2. A True Return True! We fouund it!
        i += 1
    # 3. Return False
    return False