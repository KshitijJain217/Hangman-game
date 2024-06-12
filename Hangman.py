import random

# Logo for the game
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

# Stages of the Hangman
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Choose a random word from the list
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Number of lives player has
lives = 6

# Print the chosen word for debugging purposes
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ['_'] * word_length

# Keep track of already guessed letters
guessed_letters = set()

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
    else:
        guessed_letters.add(guess)

        # Check if the guessed letter is in the chosen word
        if guess in chosen_word:
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
        else:
            # Decrease the number of lives if the guess is incorrect
            lives -= 1
            print(f"Wrong guess. You have {lives} lives left.")

            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was {chosen_word}.")
                break

    # Display the current state of the word
    print(' '.join(display))

    # Check if the player has won
    if '_' not in display:
        end_of_game = True
        print("You win!")

    # Display the current stage of the Hangman
    print(stages[lives])
