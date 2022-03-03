"""EX06 - Dictionary Functions."""

__author__ = "730327035"


def invert(z: dict[str, str]) -> dict[str, str]:
    """Give a dictionary, invert the value and the keys and raise an error if duplicated."""
    invertz: dict[str, str] = {}
    for key in z:
        avalue: str = z[key]
        if avalue in invertz:
            raise KeyError("Error! More than one of the same key!")
        else:
            invertz[avalue] = key
    return invertz


def favorite_color(namescolor: dict[str, str]) -> str:
    """Given a dictionary for names and color it returns the most popular color."""
    colors: dict[str, int] = {}
    for key in namescolor:
        pigment: str = namescolor[key]
        if pigment in colors:
            colors[pigment] += 1
        else:
            colors[pigment] = 1 
    popular: int = 0 
    result: str = ""
    for key in colors:
        if colors[key] > popular:
            popular = colors[key]
            result = key 
    return result


def count(a: list[str]) -> dict[str, int]:
    """Counting the amount of times a variable appears."""
    empty: dict[str, int] = {}
    for item in a:
        if item in empty:
            empty[item] += 1
        else:
            empty[item] = 1
    return empty
