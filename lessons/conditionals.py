"""An example of conditional (ifelse) statements."""

SECRET: int = 3

print("I am thinking of a nuumber between 1 and 5. What is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed to high!")
    else:
        print("You guessed too low!!")



print("Game over.")
