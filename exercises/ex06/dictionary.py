
"""EX06 Dictionaries."""


__author__ = "730319713"


def invert(ordered: dict[str, str]) -> dict[str, str]: 
    """Given an ordered dictionary, the keys of the input become the list of output."""
    reordered: dict[str, str] = dict()
    for symbol in ordered:
        if ordered[symbol] in reordered:
            raise KeyError("Incorrect Usage")
        reordered[ordered[symbol]] = symbol
    return (reordered)


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    mode: int = 0
    compdict: dict[str, int] = {}
    fvcolor: str = ""
    for shade in colors:
        col: str = colors[shade]
        if col in compdict:
            compdict[col] += 1
        else:
            compdict[col] = 1
    for fav in compdict:
        if compdict[fav] > mode:
            mode = compdict[fav]
            fvcolor = fav 
    return fvcolor


def count(list1: list[str]) -> dict[str, int]:
    """Generates dict with count of the number of times value appeared."""
    buildup: dict[str, int] = {}
    for item in list1:
        if item in buildup:
            buildup[item] += 1
        else: 
            buildup[item] = 1
    return buildup