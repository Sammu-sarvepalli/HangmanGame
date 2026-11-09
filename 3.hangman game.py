import random
import hangman_stages
import word_list
lives = 6
choosen_word = random.choice(word_list.words)
print(choosen_word)
display = []
for i in range(len(choosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guess = input("Guess the letter:").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = guess
    print(display)
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            game_over =  True
            print("you loose!")
    if '_' not in display:
        game_over = True
        print("You win!")
    print(hangman_stages.stages[lives])