from tkinter import *


def button_clicked():
    label["text"] = user_input.get()


# Tela = Tk()
screen = Tk()
screen.title("Eai mano")
screen.minsize(500, 500)

# Escrita = Label()
label = Label(text="Tudo bom mano", font=("Courier", 15))
label.grid(column=0, row=0)

# Botões = Button()
button = Button(text="Click Me!", command=button_clicked)
button2 = Button(text="bt2 mn")
button.grid(column=1, row=1)
button2.grid(column=2, row=0)
# Caixas de texto = Entry()
user_input = Entry()
user_input.grid(column=3, row=2)







screen.mainloop()
