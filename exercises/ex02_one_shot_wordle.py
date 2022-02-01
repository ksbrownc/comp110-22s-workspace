"""EX02- One-Shot Wordle - Loops!"""

__author__ = "730327035"


index_tracer: int = 0
SECRET = "python"
alt_index: int = 0

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
result: str = ""
wordle: bool = False

guessed_letters: str = input(f"What is your 6-letter guess? ")
while len(guessed_letters) != len(SECRET):
    guessed_letters = input((f"That was not 6 letters! Try again: "))
while index_tracer < len(SECRET):
    alt_index = 0
    if guessed_letters[index_tracer] == SECRET[index_tracer]:
        result = result + green_box
    else:
        wordle = False
        while not wordle and alt_index < len(SECRET):
            if guessed_letters[index_tracer] == SECRET[alt_index]:
                wordle = True 
            else:
                alt_index = alt_index + 1
        if wordle:
            result = result + yellow_box 
        else:        
            result = result + white_box      
    index_tracer = index_tracer + 1
print(result)
if guessed_letters == SECRET: 
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
