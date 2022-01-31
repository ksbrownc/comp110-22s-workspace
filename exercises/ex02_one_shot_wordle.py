"""EX02- One-Shot Wordle - Loops!"""

__author__ = "730327035"


i: int = 0
SECRET = "python"
wordle: bool = True
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

guessed_letters: str = input("What is your 6-letter guess? ")
while wordle:
    if len(guessed_letters) != 6:
        input(("That was not 6 letters! Try again: "))
        wordle = False
    else:
        if guessed_letters != SECRET:
            print("Not quite. Play again soon!")
    if guessed_letters == SECRET:
        print("Woo! You got it!")
        exit()

