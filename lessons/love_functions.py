
def love(name: str) -> str:
    """ Given a name as a parameter, returns a loving string."""
    return f"I love you {name} !"
#function always start with def, followed by funtion name then parameter list, special variable declaraction
#make sure there is a colon at the end. specify the return type with a dash & arrow the return with the return type


def spread_love(to:str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note