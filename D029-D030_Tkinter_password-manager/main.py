from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)

    if len(password_entry.get()) == 0:
        password_entry.insert(0, password)
    else:
        password_entry.delete(0, END)
        password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    site = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {f"{site}": {
        "email": email,
        "password": password
        }
    }

    # Se o usuário não escrever nada em alguma das caixas, a função acaba.
    if site == "" or email == "" or password == "":
        messagebox.showwarning("Oops", "Please don't leave any of the fields empty!")
    else:
        # Tentar ler um arquivo ja existente
        try:
            with open("data.json", mode="r") as data_file:
                # Lendo os dados do arquivo .json e transformando em um dict
                data = json.load(data_file)
                # Adicionando mais um item no dict
                data.update(new_data)
        # Se o arquivo não existir, cria um arquivo novo com as informações passadas
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        # Se a tentativa for bem sucedida la em cima executa o código abaixo.
        else:
            with open("data.json", mode="w") as data_file:
                # Escrevendo o dict atualizado no arquivo .json
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo("Success!", "Information saved successfully!")
            website_entry.focus()

# ------------------------- SEARCH PASSWORD ---------------------------- #


def search_password():
    item = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning("No passwords", "You don't have passwords saved yet!")
    else:
        with open("data.json", mode="r") as data_file:
            data_dict = json.load(data_file)
            if item in data_dict:
                messagebox.showinfo(item, f"e-mail: {data_dict[item]['email']}\n"
                                          f"Password: {data_dict[item]['password']}")
            else:
                messagebox.showwarning("Site not found", "Site does not exist in database.\n")


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
'''Esse argumento sticky="EW" se refere até aonde o widget vai esticar em relação
 ao widget mais largo (nesse caso eh o botão Add la embaixo).'''
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
search_button = Button(text="Search", command=search_password)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
