import random
words = ['priya', 'jaya', 'shweta', 'pinnu', 'mona', 'homeman', 'spiderman', 'superman']

def choose_word():
    """Randomly select a word from the list"""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the word with blanks for unguessed letters"""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()  # Select a random word
    guessed_letters = []  # List of letters guessed by the player
    incorrect_guesses = 0  # Number of incorrect guesses
    max_incorrect_guesses = 5
    # Maximum allowed incorrect guesses
    print("Welcome to Hangman!")
    print("Try to guess the word.")

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess.isalpha() and len(guess) == 1:  # Check if the input is a valid letter
            guessed_letters.append(guess)

            if guess not in word:
                incorrect_guesses += 1
                print(f"Incorrect! '{guess}' is not in the word.")
            else:
                print(f"Good job! '{guess}' is in the word.")
        else:
            print("Invalid input. Please enter a single letter.")

        # Check if the word is completely guessed
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break

    # Game over
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
