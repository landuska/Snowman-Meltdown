import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_ATTEMPTS = 3


def get_random_word():
    """Selects a random word from the list."""

    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """This function displays the game state."""

    print("-" * 40)
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: " + display_word.strip())
    print("-" * 40)


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = set()

    print("*" * 40)
    print("***** Welcome to Snowman Meltdown! *****")
    print("*" * 40)

    while mistakes < len(STAGES) - 1:

        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower().strip()

        if guess in guessed_letters:
            print("You already guessed that letter")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("well done!")
        else:
            mistakes += 1
            print("sorry, that letter is not in the word")
            print(f"You used {mistakes} attempt out of {MAX_ATTEMPTS}")

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You guessed the word!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("-" * 40)
    print(f"Game over! The word was: {secret_word}")
