"""One-shot wordle."""

__author__: str = "730577405"

secret: str = "python"
number: int = int(len(secret))
guess: str = input(f"What is your { number}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
stuff: str = ""
i: int = 0

while int(len(guess) != len(secret)):
    guess = str(input(f"That was not {number} letters! Try again: "))

if (int(len(guess)) == int(len(secret))):
    while(i < int(len(secret))):
        if guess[i] == secret[i]:
            stuff = stuff + GREEN_BOX
        else:
            letter_exists = False
            j: int = 0
            while letter_exists == False and j < int(len(secret)):
                if secret[j] == guess[i]:
                    letter_exists = True
                j += 1
            if letter_exists == True:
                stuff += YELLOW_BOX
            else:
                stuff = stuff + WHITE_BOX
        i = i + 1
    print(stuff)

if (guess == secret):
    print("Woo! You got it!")

if (guess != secret and int(len(guess)) == int(len(secret))):
    print("Not quite. Play again soon!")