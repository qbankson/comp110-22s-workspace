"""Wordle EX03"""

__author__ = "730319713"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(sthrough: str, sfor: str) -> bool:
    """When given two strngs, will return True if the single charcter of sfor is found within sthrough."""
    assert len(sfor) == 1 
    charcount: int = 0
    while charcount < len(sthrough):
        if sthrough[charcount] == sfor:
            return bool(True)
        else:
            charcount += 1
    return bool(False)


def emojified(aguess: str, asecret: str) -> str: 
    """Test for yellow or white codification."""
    assert len(aguess) == len(asecret)
    coder: int = 0 
    result: str = ""
    while coder < len(aguess): 
        if bool(contains_char(asecret, aguess[coder])) == False: 
            result = result + WHITE_BOX
        elif bool(contains_char(asecret, aguess[coder])) == True:
            if aguess[coder] == asecret[coder]:
                result = result + GREEN_BOX
            else:
                result = result + YELLOW_BOX
        coder += 1
    return f"{result}"


def input_guess(strln: int) -> str:
    """Prompt for expected length."""
    response: str = input(f"Enter a {strln} character word: ")
    while len(response) != strln:
        response = str(input(f"That wasn't {strln} chars! Try again: "))
    return f"{response}"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    N: int = 0
    wordleotd: str = "codes"
    while (N < 6 and ((wordleotd) != input_guess)): 
        print(f"=== Turn {N+1}/6 ===")
        print(emojified(str(input_guess(len(wordleotd))), (wordleotd)))
        N = N + 1
        if str(input_guess) == wordleotd:
            return print(f"You won in {N}/6 turns!")
    if (str(wordleotd) != str(input_guess)):
        return print(str("X/6 - Sorry, try again tomorrow"))


from exercises.ex03_wordle import contains_char
from exercises.ex03_wordle import emojified 
from exercises.ex03_wordle import input_guess
from exercises.ex03_wordle import main

print(main())
        







        









    
