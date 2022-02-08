"""Ex03 - Structured Wordle."""

__author__ = "730327035"


white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

result: str = ""


def contains_char(word: str, single: str) -> bool: 
    """Returns true or false given character."""
    assert len(single) == 1
    i: int = 0
    while i < len(word):
        # At this point in coding we are seing if given the strings that there is an instance where a certain character is found in the word.
        if word[i] == single:
            return True
        i += 1
        # if there is no instance of the character found at any index of the word.
    return False
    
    
def emojified(guess: str, secret: str) -> str: 
    """Returns emoji that codifies to word."""
    assert len(guess) == len(secret)
    result: str = ""
    i: int = 0
    # given a guess, the function emojified will implement colored emoji boxes whether the guess has similar indexes with the secret word or if there is an index but at another place.
    while i < len(guess):
        if guess[i] == secret[i]:
            result = result + green_box
        elif contains_char(secret, guess[i]):
            result = result + yellow_box
        else:
            result = result + white_box
        i += 1
    return result


def input_guess(expected: int) -> str: 
    """Returns guessed word if it meets the expected length."""
    # based on the length of the secret that is the expected character word in which this prompts the guess word. If the guess word is not the expected then it would prompt the system to try again. 
    guessed_word = input(f"Enter a {expected} character word: ")
    while len(guessed_word) != expected: 
        guessed_word = input((f"That wasn't {expected} chars! Try again: "))
    return guessed_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET = "codes"
    turns: int = 0
    won: bool = False
    # The main function prompts a loop using the previous functions to determine if the guessed words is the secret and how many turns it took to get it a full win.
    while turns < 6 and won is not True:
        print(f"=== Turn {turns + 1}/6 ===")  
        guessed_word = input_guess(len(SECRET)) 
        print(emojified(guessed_word, SECRET))
        turns += 1
        if guessed_word == SECRET:
            won = True
    if won: 
        print(f"You won in {turns}/6 turns! ")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
# this makes the system import the other functions created into the main function and make the coding process possible.
    