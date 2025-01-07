import random
import hangman_words as words
import hangman_art as art


print(art.logo)
lives = 6

chosen_word = random.choice(words.word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    if guess in correct_letters:
        print(f"You already guessed '{guess}', try a different one")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        print(f"\nYou guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"The word was '{chosen_word}', good luck next time!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(art.stages[lives])
