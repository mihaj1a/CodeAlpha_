import random

# Step 1: Predefined list of 5 words
word_list = ['apple', 'house', 'table', 'chair', 'plant']
secret_word = random.choice(word_list)

# Step 2: Game setup
guessed_letters = []         # letters guessed by player
tries_left = 6               # max wrong guesses allowed
display_word = ['_'] * len(secret_word)  # word display with underscores

print("🎮 Welcome to Hangman!")
print("Guess the word:", ' '.join(display_word))

# Step 3: Main game loop
while tries_left > 0 and '_' in display_word:
    guess = input("Enter a letter: ").lower()

    # Step 4: Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Step 5: Check if guess is correct
    if guess in secret_word:
        print("✅ Correct guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        tries_left -= 1
        print(f"❌ Wrong guess! Tries left: {tries_left}")

    # Step 6: Show current progress
    print("Word:", ' '.join(display_word))

# Step 7: Game result
if '_' not in display_word:
    print(f"\n🎉 You win! The word was: {secret_word}")
else:
    print(f"\n💀 You lost! The word was: {secret_word}")
