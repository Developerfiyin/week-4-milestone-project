
"""
Welcome to the Secret Word Challenge!
Use the hints to discover the hidden word before you run out of attempts.
Correct letters become UPPERCASE, misplaced letters become lowercase,
and letters that are not in the word become underscores.
"""

secret_word = "planet"
guess_count = 0
max_guesses = 5

# Create the initial hint using a loop
hint = ""

for letter in secret_word:
    hint += "_ "

print(" SECRET WORD CHALLENGE ")
print("Your starting hint is:")
print(hint)

# Keep asking for guesses until the word is correct or attempts run out
while guess_count < max_guesses:

    guess = input("\nEnter your guess: ").lower()
    
    # Check the length of the guess
    if len(guess) != len(secret_word):
        print(" Your guess must have", len(secret_word), "letters.")
        continue

    guess_count += 1

    # Check if the guess is correct
    if guess == secret_word:
        print("\n AMAZING! You found the secret word!")
        print("The word was:", secret_word)
        print("You found it in", guess_count, "guess(es)!")
        break

    # Create the hint
    hint = ""

    for index in range(len(secret_word)):

        # Correct letter in the correct position
        if guess[index] == secret_word[index]:
            hint += guess[index].upper() + " "

        # Letter exists somewhere else in the secret word
        elif guess[index] in secret_word:
            hint += guess[index].lower() + " "

        # Letter does not exist in the secret word
        else:
            hint += "_ "

    print("Hint:", hint)
    print("Guesses remaining:", max_guesses - guess_count)

else:
    print("\n GAME OVER!")
    print("You used all", max_guesses, "guesses.")
    print("The secret word was:", secret_word)

print("\nThanks for playing! ")





# number = int(input("Please type a postive number?  ")) 
# while number < 0:
#     print("Sorry, that is a negative number. Please try again.")
#     number = int(input("Please type a positive number: "))

# print(f"The number is: {number}")

# answer = ""
# while answer != "yes":
#     # This could be written as: 'while answer == "no":'
#     # The difference would be how it treats other words, besides yes and no
#     answer = input("May I have a piece of candy? ")

# print ("Thank you.")