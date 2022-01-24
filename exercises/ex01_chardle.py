"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730327035"

i: int = 0
five_characters: str = input("Enter a 5-character word: ")
if (len(five_characters)) != 5: 
    print("Error: Word must contain 5 characters ")
    exit()
else: 
    single_character: str = input("Enter a single character: ")
    counter: int = 0
    if len(single_character) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print("Searching for " + single_character + " in " + five_characters)

        if five_characters[0] == single_character:
            print(single_character + " found at index 0")
            counter = counter + 1
        if five_characters[1] == single_character:
            print(single_character + " found at index 1")
            counter = counter + 1
        if five_characters[2] == single_character:
            print(single_character + " found at index 2")
            counter = counter + 1
        if five_characters[3] == single_character:
            print(single_character + " found at index 3")
            counter = counter + 1
        if five_characters[4] == single_character:
            print(single_character + " found at index 4")
            counter = counter + 1
            
        if counter == 1:
            print(str(counter) + " instance of " + single_character + " found in " + five_characters) 
        if counter == 0:
            print(" No instances of " + single_character + " found in " + five_characters)
        if counter > 1:
            print(str(counter) + " instances of " + single_character + " found in " + five_characters)
        else:
            print(str(counter) + " instances of " + single_character + " found in " + five_characters)
