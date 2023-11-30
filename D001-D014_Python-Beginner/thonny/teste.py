with open("C:/Users/arthu/OneDrive/03_Estudos/Curso Python/100 Days of Coding/Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as name_file:
    list_of_names = name_file.readlines()

with open("C:/Users/arthu/OneDrive/03_Estudos/Curso Python/100 Days of Coding/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as invitation:
    texto = invitation.read()
for name in list_of_names:
    new_name = name.strip("\n")
    with open(f"C:/Users/arthu/OneDrive/03_Estudos/Curso Python/100 Days of Coding/Mail Merge Project Start/Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as convite:
        texto = texto.replace("[name]", new_name)
        convite.write(texto)