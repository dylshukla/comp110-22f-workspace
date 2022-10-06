"""What Organelle Are You?"""

__author__: str = "730577405"

import random

points: int = 0
player: str = ""
EMOJI_1: str = "\U0001F928"
EMOJI_2: str = "\U0001F31E"
EMOJI_3: str = "\U0001F644"
EMOJI_4: str = "\U0001F62D"


def main() -> None:
    """Main function for game."""
    global points
    greet()
    options: str = input("You can choose to end the game, try to earn an extra point through the access code, or just bypass our security measures and take the quiz. End, try, or bypass? ")
    if options == "end":
        print("Wow... ok don't ever try it then.")
        quit()
    if options == "try":
        access_quiz()
        points += quiz(0)
    if options == "bypass":
        points += quiz(0)
    if points >= 9:
        print("You would be a great mitochondria! Your need for leadership and drive for power are what make you whole.")
    elif points >= 5 and points < 9:
        print("We see you as a chloroplast. Fun and bright!")
    elif points >= 3 and points < 5:
        print("You are definitely the brains.")
    elif points < 3:
        print("We believe a lysosome would fit you best. Not first but not the worst.")


def greet() -> None:
    """Game start greeting for player."""
    print("Welcome to 'Which Organelle Are You?!' In this game you will answer a series of question to see what kind of organelle best suits your personality.")
    global player
    player = input("What is your name? ")
    

def access_quiz() -> None:
    """Access code to reach quiz questions."""
    global points
    print("First we have to see whether you are able to access our premium subscription! In order to play the quiz, input the number (from 1 to 3) that is the access code to this quiz.")
    print("If you guess on the first try, you have the option to take a free point! Guess here: ")
    code: str = input()
    r1 = random.randint(1, 3)
    attempts: int = 1
    while int(code) != r1:
        code = str(input("That was the wrong access code. Try again: "))
        attempts += 1
    print("Perfect!! Time to start the quiz!")
    if attempts == 1:
        question_5: str = input("Would you like to receive a free point? yes or no: ")
        if str(question_5) == "yes":
            points += 1


def quiz(points: int) -> int:
    """Quiz questions for player."""
    global answer
    question_1: str = input(f"Here is question 1. Do you enjoy taking charge of sitations and being perceived as the most important person in a group?{EMOJI_1} Answer yes or no: ")
    if str(question_1) == "yes":
        points += 5
    question_2: str = input(f"Onto question 2. Would you describe yourself as 'colorful' or outgoing and someone who loves being out in the sun?{EMOJI_2} Again, answer yes or no: ")
    if str(question_2) == "yes":
        points += 4
    question_3: str = input(f"Question 3... Are you the kind of person that feels the need to show everyone your intellect and outsmart and calculate their every move?{EMOJI_3} yes or no... ")
    if str(question_3) == "no":
        points += 2
    question_4: str = input(f"Do you like just sitting and eating junk food?{EMOJI_4} yes or no: ")
    if str(question_4) == "yes":
        points += 1
    return points
    

if __name__ == "main":
    main()