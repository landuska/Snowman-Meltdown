import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: " + display_word.strip())


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = set()

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    while mistakes < len(STAGES) - 1:

        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower().strip()

        if guess in guessed_letters:
            print("You already guessed that letter")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("well done!")
        else:
            mistakes += 1

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You guessed the word!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Game over! The word was: {secret_word}")
