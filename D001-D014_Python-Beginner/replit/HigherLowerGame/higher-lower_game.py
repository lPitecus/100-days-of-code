import random
from game_data import data
from art import logo, vs
import os

def get_informations(chosen_account):
    '''Escolhe uma conta aleatória dentre as disponíveis e retorna uma string com o nome, descrição e país da conta'''

    return chosen_account["name"]+', a '+chosen_account["description"]+', from '+chosen_account["country"]+'.'

def get_followers(chosen_account):
    '''Retorna a quantidade de seguidores de uma conta escolhida (dicionário com as informações)'''
    
    return chosen_account["follower_count"]

def get_answer():
    '''Compara as duas contas e retorna uma string que representa a opção com mais seguidores'''
    a_followers = get_followers(chosen_account_1)
    b_followers = get_followers(chosen_account_2)
    if a_followers > b_followers:
        return "a"
    else:
        return "b"

chosen_account_1 = random.choice(data)
chosen_account_2 = random.choice(data)
points = 0
game_over = False
print(logo)
while not game_over:
    answer = get_answer()
    print(f"the answer is {answer}")
    print("Compare A:",get_informations(chosen_account_1))
    print(vs)
    print("Against B:", get_informations(chosen_account_2))
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == answer:
        chosen_account_1 = chosen_account_2
        chosen_account_2 = random.choice(data)
        points += 1
        os.system("clear")
        print(logo)
        print(f"You're right! Current score {points}")
    else:
        os.system("clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {points}")
        game_over = True