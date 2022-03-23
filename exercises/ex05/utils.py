"""EX05 List Utility Functions."""


__author__ = "730319713"


def only_evens(digits: list) -> list[int]:
    """Construct inclusive list of only evens."""
    evnlist: list[int] = list()
    for even in digits:
        if even // 2 == even / 2:
            evnlist.append(even)
    return evnlist 


def sub(index: list, start: int, end: int) -> list[int]:
    """Generate a subset of a list."""
    set: int = len(index)
    n: int = start
    newlist: list[int] = list() 
    if set == 0 or start >= set or end <= 0 or end > set or (end - 1 > set):
        return newlist
    x: int = 0
    if start < 0:
        while x <= (end - 1):
            newlist.append(index[x])
            x += 1 
        return newlist
    while n <= (end - 1):
        newlist.append(index[n])
        n += 1 
    return newlist 


a_list: list[int] = [10, 20, 30, 40]
print(sub(a_list, 0, 3))


def concat(lone: list, ltwo: list) -> list[int]:
    """Generates a new list containing lone followed by ltwo."""
    conlist: list[int] = list()
    for item in lone:
        conlist.append(item)
    for digit in ltwo:
        conlist.append(digit)
    return conlist