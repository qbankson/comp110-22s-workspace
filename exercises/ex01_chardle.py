"""EX01 - Chardle - A Cute Step Toward Wordle."""

__author__ = "730319713"
wordchoice: str = input("Enter a 5-character word: ")
if len(wordchoice) == 5: 
    ltrchoice: str = input("Enter a single character: ")
    if len(ltrchoice) == 1: 
        print("Searching for " + ltrchoice + " in " + wordchoice)
        counter: int = 0
        if ltrchoice == wordchoice[0]: 
            print(ltrchoice + " found at index 0") 
            counter = counter + 1 
        if ltrchoice == wordchoice[1]: 
            print(ltrchoice + " found at index 1") 
            counter = counter + 1 
        if ltrchoice == wordchoice[2]: 
            print(ltrchoice + " found at index 2") 
            counter = counter + 1 
        if ltrchoice == wordchoice[3]: 
            print(ltrchoice + " found at index 3") 
            counter = counter + 1 
        if ltrchoice == wordchoice[4]: 
            print(ltrchoice + " found at index 4") 
            counter = counter + 1 
        if ltrchoice != wordchoice[0] and ltrchoice != wordchoice[1] and ltrchoice != wordchoice[2] and ltrchoice != wordchoice[3] and ltrchoice != wordchoice[4]:
            print("No instances of " + ltrchoice + " found in " + wordchoice)
        if counter == 1: 
            print(str(counter) + " instance of " + ltrchoice + " found in " + wordchoice)
        if counter == 2: 
            print(str(counter) + " instances of " + ltrchoice + " found in " + wordchoice)
        if counter == 3:
            print(str(counter) + " instances of " + ltrchoice + " found in " + wordchoice)
        if counter == 4: 
            print(str(counter) + " instances of " + ltrchoice + " found in " + wordchoice)
        if counter == 5: 
            print(str(counter) + " instances of " + ltrchoice + " found in " + wordchoice)
    else: 
        print("Error: Character must be a single character. ")
        exit()
else: 
    print("Error: Word must contain 5 characters")
    exit()
