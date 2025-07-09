import random

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

WORDS = ['python', 'machine', 'learning', 'data', 'science', 'hangman', 'developer', 'github']

def get_random_word():
    return random.choice(WORDS)

def display_game_state(hangman_pics, missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print("\nMissed letters:", ' '.join(missed_letters))

    blanks = ['_' if letter not in correct_letters else letter for letter in secret_word]
    print("Word: ", ' '.join(blanks))

def get_guess(already_guessed):
    while True:
        guess = input("\nGuess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You already guessed that letter.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        else:
            return guess

def play():
    print("🎮 Welcome to Hangman - Python Edition!")
    secret_word = get_random_word()
    missed_letters = []
    correct_letters = []

    game_over = False

    while not game_over:
        display_game_state(HANGMAN_PICS, missed_letters, correct_letters, secret_word)

        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters.append(guess)

            found_all_letters = all(letter in correct_letters for letter in secret_word)
            if found_all_letters:
                print(f"\n✅ Congratulations! You guessed the word: {secret_word}")
                game_over = True
        else:
            missed_letters.append(guess)

            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_game_state(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                print(f"\n❌ You've been hanged! The word was: {secret_word}")
                game_over = True

    if input("\nPlay again? (y/n): ").lower().startswith('y'):
        play()

if __name__ == '__main__':
    play()
