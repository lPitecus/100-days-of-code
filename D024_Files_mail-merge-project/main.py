# abrindo o documento com os nomes dos convidados
with open("Input/Names/invited_names.txt", mode="r") as name_file:
    # criando uma lista com esses nomes com a função readlines()
    list_of_names = name_file.readlines()

# criando uma variável que contém o texto base do convite
with open("Input/Letters/starting_letter.txt", mode="r") as invitation:
    letter_content = invitation.read()

# para cada nome na lista de nomes
for name in list_of_names:
    # tratar o nome retirado do documento
    new_name = name.strip("\n")
    # criar um convite a partir do texto base trocando a pare [name] pelo nome dos convidados.
    with open(f"Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as convite:
        new_letter = letter_content.replace("[name]", new_name)
        convite.write(new_letter)
