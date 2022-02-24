"""Example of a function that searches through a list."""

def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davison"]))
# Define a function named contains
#Two parameters:
    #1. needle- the string we're searching for
    #2.haystack - the list we're searching through
def contains(needle: str, haystack: list[str]) -> bool:
    #Algorithm:
        #for each item in the haystacks
        #test if it is equal to the needle 
        #   If so, return true
    for item in haystack:
            if item == needle:
                return True
    #after testing all items return false, because not found
    #returns true if needle in haystack is false otherwise
    return False

if __name__ == "__main__":
    main()

