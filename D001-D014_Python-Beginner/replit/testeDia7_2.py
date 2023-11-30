import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')


display = []
for letter in range(len(chosen_word)):
    display.append("_")

guess = input("Guess a letter: ").lower()


cont = 0
for letter in chosen_word:
    if letter == guess:
        display[cont] = letter
        cont += 1
        print(display)