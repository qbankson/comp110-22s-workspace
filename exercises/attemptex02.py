"""EX02 - One Shot Wordle."""

__author__ = "730319713"
secretwrd: str = "python"
inputwrd: str = input(f"What is your { len(secretwrd) }-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
exist: bool = False 
match: int = 0 
i: int = 0
result: str = ""
while len(inputwrd) != len(secretwrd): 
    inputwrd: str = input(f"That was not { len(secretwrd) } letters! Try again: ")
if len(inputwrd) == len(secretwrd):
    while i < len(secretwrd): 
        if secretwrd[i] == inputwrd[i]: 
            result = result + GREEN_BOX + " "
            i = i + 1

        elif secretwrd[i] != inputwrd[i]:
            while i < len(secretwrd) and bool(exist) == False:
                if secretwrd[match] == inputwrd[i]:
                    exist = True 
                else: 
                    match = match + 1 
            if bool(exist) == True: 
                result = result + YELLOW_BOX + " "
            else: 
                result = result + WHITE_BOX + " "
                    
            i = i + 1
    print(result)
if inputwrd == secretwrd: 
    print("Woo! You got it!")
    exit()

if len(inputwrd) == len(secretwrd) and inputwrd != secretwrd: 
    print("Not quite. Play again soon!") 
    exit()
