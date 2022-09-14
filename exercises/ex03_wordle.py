"""Finished Wordle."""

__author__: str = "730577405"

def contains_char(word: str, chr: str) -> bool:
    """Function to check indices and mark True/False."""
    assert len(chr) == 1
    i: int = 0
    length: int = int(len(word))
    while i < length:
        if word[i] == chr:
            return True
        else:
            i += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Loops through word and concatenates emojified boxes."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    answer: str = ""
    j: int = 0
    assert len(secret) == len(guess)
    while j < int(len(secret)):
        if guess[j] == secret[j]:
            answer = answer + GREEN_BOX
        else:
            if contains_char(secret, guess[j]):
                answer += YELLOW_BOX
            else:
                answer += WHITE_BOX
        j += 1
    return answer

def input_guess(expected: int) -> str:
    """Checks for length of guess and repeats guess based on if condition is met."""
    guess_len: str = input(f"Enter a {expected} character word: ")
    while expected != len(guess_len):
        guess_len = input(f"That wasn't {expected} chars! Try again: ")
    return guess_len

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "codes"
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            return None
        else:
            turns += 1
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()