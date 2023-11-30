pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

#Declaração de variáveis
jogada_pessoa = 0
jogada_computador = random.randint(0,2)
jogadas = [pedra, papel, tesoura]

jogada_pessoa = int(input("Bem vinde a pedra, papel e tesoura! Digite sua jogada (0 para pedra, 1 para papel e 2 para tesoura): "))

#Montagem do jogo
print("Sua jogada:\n"+jogadas[jogada_pessoa]+"\n")
print("Jogada da máquina:\n"+jogadas[jogada_computador]+"\n")

#Critérios de vitória, derrota ou empate      
if jogada_pessoa == 1 and jogada_computador == 3:
  print("Você ganhou!")

elif jogada_pessoa == 3 and jogada_computador == 2:
  print("Você ganhou!")

elif jogada_pessoa == 2 and jogada_computador == 1:
  print("Você ganhou!")

elif jogada_pessoa == jogada_computador:
  print("Empate!")

else:
  print("Você perdeu!")