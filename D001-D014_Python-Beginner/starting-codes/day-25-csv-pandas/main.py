# with open("weather_data.csv", "r") as fl:
#     data = fl.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if "temp" in row:
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())

# colocando a linha que tem "Monday" numa variável monday
# monday = data[data.day == "Monday"]
# monday_c_temp = monday.temp[0]
# monday_f_temp = (monday_c_temp * 9 / 5) + 32
# print(monday_f_temp)

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_data = data.value_counts("Primary Fur Color")
# lista com a contagem de cores de cada cor, da maior contagem para a menor
# caso tenha dúvida, imprima fur_data depois fur_list
fur_list = fur_data.to_list()
fur_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [fur_list[0], fur_list[1], fur_list[2]]
}
df = pandas.DataFrame(fur_dict)
df.to_csv("squirrel_count.csv")
print(df)

# da tabela data, analisando a coluna "Primary Fur Color", deseja-se pegar todas as linhas que contenham o valor "Gray"
tabela_filtrada = data[data["Primary Fur Color"] == "Gray"]
print(tabela_filtrada)
