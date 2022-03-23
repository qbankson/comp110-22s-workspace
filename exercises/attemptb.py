"""EX02 - One Shot Wordle Game."""

__author__ = "730319713"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
exist: bool = False 
match: int = 0 
i: int = 0
result: str = ""
secretwrd: str = "python"
inputwrd: str = input(f"What is your { len(secretwrd) }-letter guess? ")
while len(inputwrd) != len(secretwrd): 
    inputwrd = str(input(f"That was not { len(secretwrd) } letters! Try again: "))
if len(inputwrd) == len(secretwrd) and inputwrd != secretwrd: 
    while i < len(secretwrd):
        if secretwrd[i] == inputwrd[i]:
            result = result + GREEN_BOX + " "
        else:
            while exist == bool(False) and i < len(secretwrd):
                if secretwrd[match] == inputwrd[i]:
                    exist = True
                else:
                    match = match + 1
            if exist == bool(True):
                result = result + YELLOW_BOX + " "
            else:
                result = result + WHITE_BOX + " "
        i = i + 1
  
        print(result)
        print("Not quite. Play again soon!")
if inputwrd == secretwrd: 
    if secretwrd[i] == inputwrd[i]:
            result = result + GREEN_BOX + " "
    print(result)
    print("Woo! You got it!")
