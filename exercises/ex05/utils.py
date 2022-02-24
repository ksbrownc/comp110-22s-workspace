"""Ex05 - 'List' Function Skeleton Implementation."""

__author__ = "730327035"


def only_evens(only: list[int]) -> list[int]:
    """Creating an only evens function to draw even functions."""
    even_list: list[int] = []
    for item in only:
        if item % 2 == 0:
            even_list.append(item)
    return even_list
    

def sub(some_list: list[int], begin: int, finale: int) -> list[int]:
    """In the sublist function which is to take the beginning and the end of a list."""
    the_list: list[int] = []
    if begin < 0:
        begin = 0
    if finale > len(some_list):
        finale = len(some_list)
    if len(some_list) == 0 or begin > len(some_list) or finale <= 0:
        return the_list
    while begin < finale:
        the_list.append(some_list[begin]) 
        begin += 1
    return the_list


def concat(con: list[int], cat: list[int]) -> list[int]:
    """This function takes one of the first lists and combines with the second list."""
    con_cats: list[int] = []
    i: int = 0
    while i < len(con):
        con_cats.append(con[i])
        i += 1
    i = 0
    while i < len(cat):
        con_cats.append(cat[i])
        i += 1
    return con_cats
    
