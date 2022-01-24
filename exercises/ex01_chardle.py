"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730327035"

SECRET: str = "grass"

five_letters: str = input("Enter a 5-character word: ")

if five_letters == SECRET: 
    grass_word: str= input ("Enter a single character: ")
    print("Searching for " + grass_word + " in " + five_letters)
    print(grass_word + " found in index 1")
    print("1 instances of " + grass_word + " in " + five_letters)
else:
    if five_letters < SECRET:
        print("Error: word must contain 5 characters")
