"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730327035"

i:int = 0
grass_word: str = input("Enter a 5-character word: ")
five_letters: str = input("Enter a single character: ")

if grass_word[i] == five_letters: 
    print("Searching for " + five_letters + " in " + grass_word)
