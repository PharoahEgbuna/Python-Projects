import random

game_title = "Word Raider"

# Create a list for storing words
word_bank = []

# Add words to the word bank
with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

# Set unchanging game variable
max_turns = 5

# Display the initial game state
print(f"Welcome to {game_title}!")
print(f"In this game you must try to guess the correct 5-letter word within {max_turns} turns.")
print("After each turn you will be given hints on which letters you've used that don't belong in the word and correct leters used in the wrong position.\n")

# Game Loop
while True:

    # Set looping game variables
    misplaced_letters = []
    incorrect_letters = []
    turns_taken = 0

    # Pick a random word from the word bank
    random_word = random.choice(word_bank)

    # A list for saving correctly guessed and positioned letters.
    player_progress = ['_', '_', '_', '_', '_']

    while turns_taken <= max_turns:
        # Receive the player's guess
        user_guess = input("Enter your guess: ").lower()

        #Check if the player's guess is the proper length and only contains letters
        if len(user_guess) != 5 or not user_guess.isalpha():
            print("Invalid input. Please enter a 5 letter word.")
            continue

        # Check if the player has won
        if user_guess == random_word:
            print(f"Congratulations, {random_word} was correct!\n")
            break
        else: 
            turns_taken += 1

        idx = 0
        for letter in user_guess:
            if letter == random_word[idx]:
                # If the letter is correctly guessed and positioned, replace an underscore in the player_progress list
                player_progress[idx] = letter
                if letter in misplaced_letters:
                    misplaced_letters.remove(letter)
            elif letter in random_word and letter not in misplaced_letters:
                #If the letter is misplaced, add it to the misplaced list
                misplaced_letters.append(letter)
            else:
                #If the letter is incorrect, add it to the incorrect list
                incorrect_letters.append(letter)
            idx += 1

        # Check if the player has lost
        if turns_taken == max_turns:
            print(f"Sorry, you used all your turns. The correct word was: {random_word}")
            break

        # Print the player's progress
        print(f"\n{" ".join(player_progress)}\n")
        print("Misplaced letters: ", misplaced_letters)
        print("Incorrect letters: ", incorrect_letters)

        # Display the number of turns remaining
        print(f"You have {max_turns - turns_taken } turn(s) remaining.\n")
    
    play_again = input("Do you want to play again? (Yes or No) ").lower()

    # Check if user wants to quit
    if 'no' in play_again:
        print("Thanks for playing!")
        quit()