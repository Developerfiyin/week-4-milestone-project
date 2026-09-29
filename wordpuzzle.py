secret_word = "apple"
guess_count = 0

# Create the initial hint
hint = ""

for letter in secret_word:
    hint += "_ "

print("Hint:", hint)

# Keep asking for guesses
while True:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    # Check the length
    if len(guess) != len(secret_word):
        print("Your guess must have", len(secret_word), "letters.")
        continue

    
    hint = ""

    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper() + " "
        elif guess[i] in secret_word:
            hint += guess[i].lower() + " "
        else:
            hint += "_ "

    print("Hint:", hint)

    # Check if the word is correct
    if guess == secret_word:
        print("You guessed the word!")
        print("Number of guesses:", guess_count)
        break