import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


while True:
    name = input("What's your name?: ").upper()
    try:
        nato_name = [nato_dict[char] for char in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_name)
        break


