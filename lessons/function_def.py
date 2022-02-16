""" An example function defintion."""



def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b:
        return a

    return b
# print(my_max(10 + 1, 10))
# # print(my _max(-50, 100)
# result: int = my_max(-50, 100)
# print(result)


x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)