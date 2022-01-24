"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730327035"



i: int = 0
grass_word: str = input("Enter a 5-character word: ")
if (len(grass_word))!= 5: 
    print("Error: Word must contain 5 characters ")
else: 

    five_letters: str = input ("Enter a single character: ")
    counter: int = 0

    print("Searching for " + five_letters + " in " + grass_word)



    if grass_word[0] == five_letters:
        print( five_letters + " found at index 0")
        counter = counter + 1
    if grass_word[1] == five_letters:
        print( five_letters + " found at index 1")
        counter = counter + 1
    if grass_word[2] == five_letters:
        print( five_letters + " found at index 2")
        counter = counter + 1
    if grass_word[3] == five_letters:
        print( five_letters + " found at index 3")
        counter = counter + 1
    if grass_word[4] == five_letters:
        print( five_letters + " found at index 4")
        counter = counter + 1
        
    print (str(counter) + " instances of " + five_letters + " found in " + grass_word)


