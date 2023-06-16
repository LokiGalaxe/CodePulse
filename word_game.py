import random

def word_game():
    words = ["python", "programming", "game", "computer", "code"]
    word = random.choice(words).lower()
    guesses = []
    attempts = 7

    print("Welcome to the Word Game!")
    print("I have chosen a word. Can you guess what it is?")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guesses:
            print("You've already guessed that letter.")
            continue

        guesses.append(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print("Wrong! You have", attempts, "attempts left.")

        masked_word = ""
        for letter in word:
            if letter in guesses:
                masked_word += letter + " "
            else:
                masked_word += "_ "

        print(masked_word)

        if "_" not in masked_word:
            print("Congratulations! You guessed the word correctly.")
            break

    if attempts == 0:
        print("Game over! The word was", word)

word_game()
