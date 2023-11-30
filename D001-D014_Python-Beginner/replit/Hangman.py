#importação de módulos
import random

#declaração de variáveis
chosen_word = random.choice(["laranja", "pera", "abacate", "chocolatismo"])
lives = 6
display = []
for _ in range(len(chosen_word)):
    display += "_"
game_is_over = False

#introdução do jogo e pedido o input do usuario por uma letra
print(f"the chosen word is {chosen_word}")
print("HANGMAN")

while not game_is_over:
    
    print(display)
    
    guess = input("Choose a letter: ")
    
    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess 
        else:
            lives -= 1
    
    if "_" not in display:
        print("You win.")
        game_is_over = True
    elif lives == 0:
        print("You lose.")
        game_is_over = True