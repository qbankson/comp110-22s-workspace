"""EX02."""

__author__ = "730319713"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0 
result: str = " "
sword: str = "python"
exists: bool = False 
alti: int = 0
iword: str = input(f"What is your { len(sword) } letter-guess? ")
while len(iword) != len(sword):
    iword = str(input(f"That was not { len(sword) } letters! Try again: "))
if len(iword) == len(sword):
    if iword != sword: 
        while i < len(sword):
            if sword[i] == iword[i]:
                result = result + GREEN_BOX 
            else:
                alti = 0 
                exists = False 
                while alti < len(sword) and exists == False:
                    if str(sword[alti]) == str(iword[i]):
                        exists = bool(True)
                    else:
                        alti = alti + 1
                if exists == bool(True):
                    result = result + YELLOW_BOX
                else: 
                    result = result + WHITE_BOX
            i = i + 1
        print(result)
        print("Not quite. Play again soon!")
    else: 
        while i < len(sword):
            if sword[i] == iword[i]:
                result = GREEN_BOX + result + " "
            i = i + 1
        print(result)
        print("Woo! You got it!")