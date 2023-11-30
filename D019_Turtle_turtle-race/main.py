import random
from turtle import Turtle, Screen

corrida_ligada = False
tela = Screen()
tela.setup(500, 400)
aposta = tela.textinput("Faça sua aposta", "Qual tartaruga vai vencer a corrida? "
                                           "Escreva uma cor (red, orange, yellow, green, blue, purple): ")
cores = ["red", "orange", "yellow", "green", "blue", "purple"]
tartarugas = []
y = -125

for cor in cores:
    nova_tartaruga = Turtle(shape="turtle")
    nova_tartaruga.color(cor)
    nova_tartaruga.penup()
    nova_tartaruga.setpos(x=-230, y=y)
    y += 50
    tartarugas.append(nova_tartaruga)

if aposta:
    corrida_ligada = True

while corrida_ligada:
    for tartaruga in tartarugas:
        if tartaruga.xcor() > 230:
            corrida_ligada = False
            print(f"A tartaruga {tartaruga.pencolor()} ganhou!!")
            if aposta == tartaruga.pencolor():
                print("Sua aposta foi correta!!")
            else:
                print("Sua aposta foi errada unheee")
        velocidade_aleatoria = random.randint(0, 10)
        tartaruga.forward(velocidade_aleatoria)

tela.exitonclick()
