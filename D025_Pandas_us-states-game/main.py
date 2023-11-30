from turtle import Screen
from state import State
import pandas

screen = Screen()
image = "blank_states_img.gif"
screen.bgpic(image)
screen.title("U.S States Game")
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
correct_list = []

while len(correct_list) < 50:
    user_answer = screen.textinput(title=f"{len(correct_list)}/{len(states_list)} States Correct",
                                   prompt="Type a state name").title()
    if user_answer == "Exit":
        break

    if user_answer in states_list:
        # get x and y values in the data variable
        # o trecho data[data["state"] == user_answer] retorna uma tabela com uma linha
        # o trecho .iloc[0] transforma a tabela em uma série
        # o trecho .iloc[0]["x"] procura qual o valor na linha está na coluna "x"
        x_cor = data[data["state"] == user_answer].iloc[0]["x"]
        y_cor = data[data["state"] == user_answer].iloc[0]["y"]
        coordinates = (x_cor, y_cor)

        # create turtle being state name
        text = State()
        # put the name in the coordinates
        text.write_state(user_answer, coordinates)

        # put the correct state in a list
        correct_list.append(user_answer)
