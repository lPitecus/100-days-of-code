from tkinter import *


def convert():
    miles = int(user_input.get())
    kilometers = miles * 1.60934
    km_number["text"] = int(kilometers)


# screen
screen = Tk()
screen.title("Miles to Km Converter")
screen.config(padx=30, pady=30)

# labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
km_number = Label(text="0")
km_number.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# buttons
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

# entries
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

screen.mainloop()
